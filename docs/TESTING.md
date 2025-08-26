# TESTING GUIDE: OpenCV Lane Detection API - Automation QA Demo

## Markers
- `functional` - core functionality tests
- `negative` - invalid inputs, error handling
- `edge` - small/large images, grayscale, night scenes
- `performance` - latency, stability

## Running tests
```bash
pytest -m functional
pytest -m negative
pytest -m edge
pytest -m performance
```

## Test data
- `data/images/happy_path/` - clear highway images
- `data/images/no_markings/` - no-lane images
- `data/images/edge/` - small, large, grayscale, night

## Reporting
- Allure planned for future milestone
- CI pipeline will attach artifacts

