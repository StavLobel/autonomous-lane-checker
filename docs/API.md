# API CONTRACT: OpenCV Lane Detection API - Automation QA Demo

## Endpoints

### GET /health
- Returns 200 with `{"status": "ok"}`.

### GET /version
- Returns 200 with JSON version and config info.

### POST /lanes
- Accepts:
  - Multipart file upload: `image`
  - JSON with `image_b64`
- Optional params:
  - `roi_top_ratio`, `roi_bottom_ratio`
  - `canny_low`, `canny_high`
  - `hough_threshold`, `min_line_len`, `max_line_gap`
  - `return_overlay` (bool)

### Response (example)
```json
{
  "lanes": {
    "left": {"x1":120,"y1":720,"x2":300,"y2":420,"slope":-0.92},
    "right": {"x1":980,"y1":720,"x2":760,"y2":420,"slope":0.88}
  },
  "lane_width_px": 640,
  "center_offset_px": -12.5,
  "num_segments_used": 14,
  "processing_ms": 78,
  "warnings": [],
  "overlay_png_b64": null
}
```

### Error Codes
- 422: Missing/invalid inputs
- 400: Corrupt data
- 415: Unsupported file type
- 413: Payload too large

