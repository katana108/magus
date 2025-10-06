# MAGUS Reproducibility Archive v1.0

Complete package for reproducing MAGUS experiments from the paper:
**"MAGUS: A Modular Adaptive Goal and Utility System for Ethical AGI Decision-Making"**

## Quick Start

### 1. Setup environment (Linux/WSL required)
```bash
cd environment
./setup.sh
```

### 2. Run all tests
```bash
cd ../tests
./run_all_tests.sh
```

### 3. Validate results
```bash
cd ../scripts
python validate_results.py
```

### 4. Generate report
```bash
python generate_report.py
```

## Expected Results

- **M2 Tests**: 19/19 passing
- **M3 Integration**: Verified
- **M4 Pipeline**: 5/5 passing
- **Total**: 31/31 tests (100%)

## System Requirements

- **Operating System**: WSL (Windows) or Linux
- **Python**: 3.12 or higher
- **RAM**: 2GB minimum
- **Disk Space**: ~500MB
- **Internet**: Required for initial hyperon install

## Documentation

- See `docs/` for detailed architecture and design docs
- See `INSTALL.md` for troubleshooting setup
- See `tests/expected_results.md` for validation criteria

## Citation

If you use this archive in your research, please cite:

```bibtex
@article{magus2025,
  title={MAGUS: A Modular Adaptive Goal and Utility System for Ethical AGI Decision-Making},
  author={MAGUS Development Team},
  year={2025},
  note={Reproducibility archive v1.0}
}
```

## License

[License details - to be determined by user]

## Support

For issues or questions:
- See `docs/troubleshooting.md`
- Check repository issues
- Contact authors (listed in paper)

---

**Archive Version**: 1.0
**Last Updated**: October 2025
**Paper Status**: Under review
