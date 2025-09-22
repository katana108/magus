MeTTa-Motto

MeTTa-Motto is a library that allows combining the capabilities of LLMs (Large Language Models) and MeTTa. MeTTa-Motto allows calling LLMs from MeTTa scripts, which enables prompt composition and chaining of calls to LLMs in MeTTa based on symbolic knowledge and reasoning.
Simple queries to LLMs

To make simple queries to an LLM using the MeTTa-Motto library, the following commands can be used:

!((anthropic-agent) (user "What is a black hole?"))

!((chat-gpt-agent)
      (user "What is a black hole?"))

chat-gpt-agent and anthropic-agent are the agents used to make requests to the ChatGPT and Claude model respectively. Currently, MeTTa-Motto supports the following LLMs:

    ChatGPT (by OpenAI)
    Claude (by Anthropic)

but more LLMs can be added if needed, and one can also use other LLMs via LangChain integration (see below).

Additionally, it is possible to specify the version of ChatGPT or Claude, such as

(chat-gpt-agent "gpt-3.5-turbo")
(anthropic-agent "claude-3-opus-20240229")

In the example above, the agent may not be specified: !(llm (user "What is a black hole?")). In this case, the default agent (currently, chat-gpt) will be used. The messages which we send to agents as parameters have the form (ROLE "Text of the Message"). There are 3 roles for messages: user, assistant and system.

llm is a method defined in MeTTa-Motto, which passes messages to the specified agent and returns their results to MeTTa. For convenience, the keyword llm has been omitted in scripts starting from MeTTa-Motto version 0.0.7. The previous syntax:

!(llm (Agent (chat-gpt))
      (user "What is a black hole?")) ;

is now automatically included in the code for the given agent.

We've also included the open-router-agent to use the OpenRouter API for obtaining responses from LLMs:

!(import! &self motto)
!((open-router-agent) (user "Who was the 22nd President of France?"))
!((open-router-agent "openai/gpt-3.5-turbo" True) (user "Who was the 22nd President of France?"))

this agent allows to specify the model type, the second call has one more additional parameter True which means that the response should be a stream (Streaming)

As a demonstration, instead of calling LLM agents, we will use the echo-agent. This agent returns the message sent to it, including the role on whose behalf the message was sent

!(import! &self motto) ; ()
!((echo-agent)
      (user "The agent will return this text along with a role: user"))
      ; "user The agent will return this text along with a role: user"

MeTTa agents

Also, as an Agent, we can specify the path to a file with a MeTTa script, which typically has a .msa (MeTTa Script Agent) extension. This script can contain any commands (expressions) in MeTTa, and may not necessarily include queries to LLMs in it, but it is supposed to run in a certain context.

For example, let us assume, there is a file named some_agent.msa containing the following code:

( = (response)
   (if (== (messages) (user "Hello world."))
       "Hi there"
       "Bye"))

(response) is used to indicate that this is the output of the agent. The some_agent.msa can be used in another script in the following manner:

!(import! &self motto)
!((metta-script-agent "some_agent.msa")
      (user "Hello world.")) ; Hi there

or in the following manner:

!(import! &self motto)
!((metta-agent "some_agent.msa")
      (user "Hello world.")) ; Hi there

For a MeTTa agent, the new atom (= (messages) (user "Hello world.")) will be added to the MeTTa space, where the agent will load some_agent.msa. This allows (messages) to be used within some_agent.msa. Typically, .msa agents are more complex and utilize LLM responses during processing. A metta-agent executes the code in some_agent.msa upon creation, and only runs the (response) function when the __call__ method is executed. In contrast, a metta-script-agent executes the code in some_agent.msa whenever the __call__ method is invoked. This is not the only difference between the two agents. In a metta-agent, there is a field that stores an instance of the MeTTa class, which is used to execute MeTTa code. As a result, all states calculated during the execution of the .msa script will remain in memory (MeTTa space) while the script in which the MeTTa agent was created is running. For metta-script-agent an instance of the MeTTa class is created each time when the __call__ method is executed.
Functional calls

Suppose we have a function that returns the current weather for a location passed as a parameter to this function. We want to ask about the weather in natural language, e.g. "What is the weather in New York today?", and receive information about the weather in conversational format. For such cases one can describe functions and have the LLM model intelligently select and output a JSON object containing the arguments needed to call one or more functions.

The latest OpenAI and Anthropic models have been trained to both detect when a function should to be called (depending on the input) and to respond with JSON that adheres to the function signature more closely. We can describe such functions in MeTTa-Motto too. For example, for the get_current_weather function, we should first describe it within doc section and define the function behavior:

!(import! &self motto)
(= (doc get_current_weather)
   (Doc
     (description "Get the current weather for the city")
     (parameters
       (location "the city: " ("Tokyo" "New York" "London"))
     )
   )
)
(= (get_current_weather ($arg) $msgs)
   (if (contains-str $arg "Tokyo")
       "The temperature in Tokyo is 75 Fahrenheit"
       (if (contains-str $arg "New York")
           "The temperature in New York is 80 Fahrenheit"
           (concat-str (concat-str "The temperature in " $arg)
                       " is 70 Fahrenheit")
    )
  )
)
!((echo-agent)
   (user "Get the current weather for the city: London") 
   (Function get_current_weather) ; The temperature in London is 70 Fahrenheit.
)

The parameters section describes the arguments of the function that should be retrieved from the user's message. The parameters can have the following properties: name, type, description and an enum with possible values.

The type property has a specific purpose. It can be provided in the form ((: parameter Atom) "Parameter description") indicating that this parameter should be converted from the Python string to a MeTTa expression before passing to the function.

In our example, concat-str (concatenates two strings) and contains-str (which checks if the first string contains the second string) are grounded functions defined in MeTTa-Motto. echo-agent is used for the demo purpose, but in real applications it will be any agent that supports functional calls. When a functional call is used with echo-agent, arguments can be extracted from the user's message only if the message includes the function description and the parameter description concatenated with a possible value of the parameter (for example: "the city: " + London). This example is useful only for testing and demonstration purposes.
Streaming

Some LLMs has API which allows streaming responses back to a client, enabling partial results for specific requests. metta-motto supports streaming, but currently only for the chat-gpt-agent. By setting the second parameter of the chat-gpt-agent to True, the response of chat-gpt-agent will be an atom that contains a Stream object:

!((chat-gpt-agent "gpt-3.5-turbo" True) (user "How many planets are in the solar system?"))

Scripts

It is convenient to store lengthy prompts and their templates for LLMs in separate files. For this reason, one can specify the path to such a file as a parameter along with agent. While these files are also MeTTa files and can contain arbitrary computations, they are evaluated in a different context and are recommended to have .mps (MeTTa Prompt Script) extension. Basically, each such file is loaded as a MeTTa script to a space, which should contain expressions reduced to the parameters of the llm method. For example, some_template.mps file containing:

(system ("Answer the user's questions if he asks about art, music, books, for other cases say: I can't answer your question"))

can be utilized from another .metta file:

!(import! &self motto)
!((chat-gpt-agent) (Script some_template.mps)
  (user "What is the name of Claude Monet's most famous painting?"))
!((chat-gpt-agent) (Script some_template.mps)
  (user "Which city is the capital of the USA?"))

The following result will be obtained:

"Claude Monet's most famous painting is called "Impression, Sunrise."”
"I can't answer your question."

Notice that the parameters specified in the mps-file are combined with the parameters specified directly. This allows separating reusable parts of prompts and utilizing them in different contexts in a composable way. In particular, if one supposes to try different LLMs with the same prompts, Agent should not be mentioned in the .mps file.

Since prompt templates are just spaces treated as parameters to llm, they can be created and filled in directly, but this is rarely needed.

!(import! &self motto)
!(bind! &space (new-space))
!(add-atom &space (user "Table"))
!(add-atom &space (user "Window"))
!((echo-agent) (Script &space)) ; "user Table user Window"

We are using echo-agent here. The result will be a concatenation of all the provided messages.
dialog-agent

To store dialogue history during interaction with LLMs, we include a special dialogue agent. Let us consider an example. We will use the dialog-agent agent for this purpose. Since the agent will be used multiple times, let us create a binding for it:

!(bind! &chat (dialog-agent dialog.msa)))

The dialog-agent agent stores the dialogue history in a special array named history. With each new message, the history is updated. The history array can be accessed from the MeTTa script (in our example, from dialog.msa) via the (history) function.

The file dialog.msa contains the following lines.

(= (context)
   (system "You are an AI assistant.
           Please, respond correspondingly."))
(= (response)
   (llm (Messages (context) (history) (messages))))

And the dialogue can be executed:

!(&chat (user "Hello! My name is John."))
!(&chat (user "What do you know about the Big Bang Theory?"))
!(&chat (user "Do you know my name?")) ; "Yes, you mentioned earlier that your name is John. Is there anything specific you would like to know or discuss?"

After the execution of the following line:

!((dialog-agent dialog.msa) (user "Hello "))

the new atom

= (history) (Messages (user "Hello!") (assistant "Greetings, Frodo Baggins! It is a pleasure to see you. How may I be of assistance to you today?"))

will be added to the MeTTa space, created to execute dialog.msa.

dialog-agent inherits from metta-agent, this means that all states calculated during the execution of the .msa script will remain in memory (MeTTa space) while the script in which the MeTTa agent was created is running.
Retrieval Agent

Sometimes we may require passing information from various documents as parts of prompts for LLMs. However, these documents may also contain irrelevant data not pertinent to our objectives. In such cases, we can use a retrieval agent. When defining this agent, it is necessary to specify the document location or a path to one document, the chunk length for embedding creation, the desired number of chunks for the agent to return, and a designated path for storing the dataset:

!(bind! &retrieval (retrieval-agent "text_for_retrieval.txt" 200 1 "data"))

Here, text_for_retrieval.txt is the document that will be searched according to the user's request, the chunks size is equal to 200, and number of the closest chunks to return is 2. This agent computes embeddings for the provided texts and stores them in a dedicated database. In our case, we use ChromaDB, an open-source vector database. When the retrieval agent is invoked for a particular sentence, it first generates embeddings for the sentence and subsequently returns the closest chunks based on cosine distance metrics. For example, the text contains information about a scientist named John, then we can ask:

(&retrieval (user "What is John working on?"))

Here is the usage example of a retrieval agent with ChatGPT:

!(let $question "What is John working on?"
    ((chat-gpt-agent "gpt-3.5-turbo")
         (Messages
           (system
             ("Taking this information into account, answer the user question"
             (&retrieval (user $question)))
           )
           (user $question)
         )
     )
)

The retrieval agent can search not only within a single document but also across an entire folder if specified. In the following example, ./data/texts_for_retrieval is the path to the folder where additional information can be searched.

!(bind! &retrieval (retrieval-agent "./data/texts_for_retrieval" 200 1 "data"))
!(&retrieval_agent
      (user "Who made significant advancements in the fields of electromagnetism?"))

In this case, you can also specify the required document during the agent call using the special Kwargs keyword:

!((&retrieval (Kwargs (doc_name "story1.txt")))
      (user  "Who made significant advancements in the fields of electromagnetism?"))

LangChain Agents

As mentioned in this tutorial, by using py-atom and py-dot, you can invoke from MeTTa such Python objects as functions, classes, methods, or other statements. Taking this possibility into account, we have created agents in MeTTa-Motto that allow using LangChain components. LangChain is a Python framework for developing applications powered by large language models (LLMs). LangChain supports many different language models. For example, the following code uses GPT to translate text from English to French:

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
messages = [
    ("system", "You are a helpful assistant that translates English to French."),
    ("human", "Translate this sentence from English to French: I love programming."),
]
llm.invoke(messages)

The implementation of the code, provided above, in MeTTa-Motto looks like this:

!(import! &self motto)
(bind! &chat
  (langchain-agent
    ((py-atom langchain_openai.ChatOpenAI)
     (Kwargs (model "gpt-3.5-turbo") (temperature 0)))
    motto/langchain_agents/langchain_agent.msa))
!(&chat
      (system "You are a helpful assistant that translates English to French.")
      (user "Translate this sentence from English to French: I love programming."))

The grounded function langchain-agent has two parameters. The first is a chat model (in this case, langchain_openai.ChatOpenAI), which should be an instance of LangChain "Runnables" with an invoke method. The second parameter is the path to the file used to call the invoke method for the given chat model.

File motto/langchain_agents/langchain_agent.msa is a part of MeTTa-Motto library and contains the following lines:

(py-dot ((py-dot (langchain-model) invoke) &list) content)

The &list is used to store the entire message history. The grounded atom langchain-model is automatically initialized with the chat model passed to langchain-agent:

(= (langchain-model)
   ((py-atom langchain_openai.ChatOpenAI)
      (Kwargs (model "gpt-3.5-turbo") (temperature 0)))
),

The langchain-agent can be used in the same situations as the chat-gpt-agent or dialog-agent agents.

These examples add not too much for what can be done without LangChain agents. However, if one wants to use LLMs not directly supported by MeTTa-Motto or to use some other components of LangChain together with knowledge representation and symbolic processing capabilities provided by MeTTa, then calling LangChain functions from MeTTa can be very useful. LangChain offers a variety of useful tools. These tools serve as interfaces that an agent, chain, or LLM can use to interact with the world. We can use these tools directly from MeTTa. For example, the following script demonstrates the use of a tool designed to query arXiv, an open-access archive with 2 million scholarly articles across various scientific fields:

!(bind! &arxiv_tool ((py-atom langchain_community.tools.arxiv.tool.ArxivQueryRun)))
!((py-dot &arxiv_tool  invoke) "What's the paper 1605.08386 about?") ;Published: 2011-02-18 Title: Quantum Anticipation Explorer ...

This example demonstrates how to use the tool individually. The tool can also be used as part of an agent. For this purpose, there is langchain_openai_tools_agent.msa in MeTTa-Motto, which utilizes langchain.agents.AgentExecutor to execute LLM agents with the use of LangChain tools:

!(import! &self motto)
!(import! &self motto:langchain_agents:langchain_states)
!(bind! &lst (py-list ()))
!((py-dot &lst append) ((py-atom langchain_google_community.GoogleSearchRun)
    (Kwargs (api_wrapper ((py-atom   langchain_google_community.GoogleSearchAPIWrapper))))))
!(set-langchain-agent-executor  &lst)
!((metta-script-agent "motto/langchain_agents/langchain_openai_tools_agent.msa")(user  "What is the name of the airport in Cali, Colombia?")) ;"The name of the airport in Cali, Colombia is Alfonso Bonilla Aragón International Airport."

The Google search tool is used here to get the answer to the user's question. The script includes the import of the langchain_states.metta file, which contains helper functions to create and store prompts, construct langchain.agents.create_tool_calling_agent, and set parameters for langchain.agents.AgentExecutor.
Advantages of MeTTa-Motto

Using MeTTa-Motto, we can process user messages with LLMs to create new knowledge bases or extend existing ones. These knowledge bases can be further processed using MeTTa expressions and then utilized in MeTTa-Motto to solve various tasks. For example, let's consider an agent defined in the file named some_agent.msa:

(= (response)
    (_eval
        ((chat-gpt-agent)
           (system "Represent natural language statements as expressions in Scheme.
               We should get triples from statements, describing some relations between items.
               Relation of location  should be  represented with 'location' property.
               Relation of  graduated from (or studies)  should be presented as 'educated_at' property.
               For example, the sentence 'New York City is  located at the southern tip of New York State' should be transformed to
               (\"New York City\" location \"New York State\").
               'Lisbon is in Portugal' should be transformed to (\"Lisbon\" location \"Portugal\"). 
               Return cities, countries, states and universities in quotes.
               The sentence  'Ann graduated from the University of Oxford' should be transformed to (Ann educated_at \"Oxford\")
               The sentence 'John is studying mathematics at MIT' should be transformed to (John educated_at \"MIT\")
               For questions about place of study we use function study_location,  for example:
               The sentence 'Is John studying in the USA?' should be transformed to (study_location John \"USA\")
               The sentence 'Did Alan graduate from the University of USA?' should be transformed to (study_location Alan \"USA\")
               The sentence 'Did Mary study in the USA?' should be transformed to (= (study_location Mary \"USA\"))
               Return result without quotes."
           )
           (messages)
        )
    )
)

This agent converts sentences containing location or education-related information into triples, such as (Ann educated_at "Oxford") or ("New York City" location "New York State"). If someone asks about the city or country where the education was received, it converts the question into a MeTTa function. For example: Did Mary study in the USA? will be converted to (= (study_location Mary "USA"). Let's define two functions: is-located, which checks if $x is located in $y, and study_location, which checks if $x studied at a place that is located in $y.

(= (is-located $x $y)
   (case (match &self ($x location $z) $z)
       (
           (Empty False)
           ($z (if  (== $z  $y) True (is-located $z $y) ))
       )
   )
)

(= (study_location $x $y)
   (case (match &self ($x educated_at $z) $z)
       (
           (Empty False)
           ($z (if  (== $z  $y) True (is-located $z $y) ))
       )
   )
)

Then, using the some_agent.msa, we can add certain relations to the meta space based on the provided facts in natural language, and verify certain facts about the place of study.

!(import! &self motto)
(Fact "Harvard is located in Massachusetts state")
(Fact "Massachusetts state is located in United States")
(Fact "Ann graduated from Harvard.")

!(match &self (Fact $fact)
  (let $expr ((metta-script-agent "some_agent.msa") (user $fact))
       (add-atom &self $expr))
 )

!(get-atoms &self)
!((metta-script-agent "some_agent.msa") (user "Did Ann study in the United States?")) ;True

This is a straightforward example demonstrating the potential of Metta-Motto to integrate MeTTa functionality with the capabilities of LLMs.
Running Metta-motto in Python

It is possible to call MeTTa-Motto agents directly from python code:

from motto.agents import  MettaAgent
agent = MettaAgent(code = '''
    (= (response) ((echo-agent) (messages)))
    ''')
print(agent('(user "Hello")').content)

In this example, an instance of MettaAgent is created using the code argument, which contains a script that defines the agent's behavior. Alternatively, the agent can be initialized with the path argument instead of code. The path should point to a .mps file containing the script to be executed to get a response from the agent. Similarly, we can use DialogAgent, which inherits all methods of MettaAgent and additionally stores dialogue history. This is the dialog-agent described above. It is possible to pass additional information, and the method call is executed for either MettaAgent or DialogAgent.

For example, let's say the file some_agent.msa contains a script:

(= (respond)
   ((chat-gpt-agent (model_name) (is_stream) True) (Messages (history) (system (system_msg)) (media (media_msg)) (messages)))
)
(= (response) (respond))

here (system_msg) and (media_msg) should be passed to agent during execution.

from motto.agents import  MettaAgent
agent = MettaAgent()
v = agent('(user "What is a black hole?")',
          additional_info=[("system_msg", long, 'String'),
                           ("model_name", "gpt-4o", 'String'),
                           ("is_stream", True, 'Bool'), ""]).content
stream = v[0].get_object().content
for chunk in stream:
    print(chunk.choices[0].delta.content)

This script sends a request to the ChatGPT model gpt-4o. Since is_stream is set to True, the response is returned incrementally in chunks through an event stream. In Python, you can iterate over these events using a for loop.