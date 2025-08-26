# Progress Tracking

This document tracks progress on all GitHub issues created from `docs/TASKS.md`.

## Summary

- **Total Issues**: 56
- **Epics**: 7
- **Major Tasks**: 25
- **Minor Tasks**: 24
- **Status**: Foundation epic complete, ready for feature development

## Epic Progress

### ALC-EP001: Foundation (P0) - 8 tasks ✅ **COMPLETE**
- [x] **#8** [ALC-EP001-M01] Scaffold project structure per SRD (Major, P0)
- [x] **#9** [ALC-EP001-M02] FastAPI app bootstrap in src/api/main.py (Major, P0)
- [x] **#10** [ALC-EP001-M03] Configuration module config.py (Major, P1)
- [x] **#11** [ALC-EP001-M04] Dockerfiles and docker-compose.yml (Major, P0)
- [x] **#12** [ALC-EP001-M05] Add Python dependencies (Major, P0)
- [x] **#13** [ALC-EP001-m01] Provide config/settings.example.env (Minor, P2)
- [x] **#14** [ALC-EP001-m02] Add .gitignore and tooling configs (Minor, P2)
- [ ] **#15** [ALC-EP001-m03] Seed data/images sample set (Minor, P2) - *Deferred*

**Progress**: 7/8 (87.5%) - Foundation complete, ready for feature development

### ALC-EP002: Lane Detection Feature (P0) - 12 tasks
- [ ] **#16** [ALC-EP002-M01] OpenCV pipeline: grayscale → blur → Canny (Major, P0)
- [ ] **#17** [ALC-EP002-M02] ROI trapezoid masking (Major, P0)
- [ ] **#18** [ALC-EP002-M03] HoughLinesP detection (Major, P0)
- [ ] **#19** [ALC-EP002-M04] Separate left/right by slope; average lines (Major, P0)
- [ ] **#20** [ALC-EP002-M05] Compute metrics (width, center offset, segments, ms) (Major, P0)
- [ ] **#21** [ALC-EP002-M06] Overlay drawing and optional base64 output (Major, P1)
- [ ] **#22** [ALC-EP002-M07] Pydantic schemas for request/response (Major, P0)
- [ ] **#23** [ALC-EP002-M08] Implement POST /lanes and wire into main.py (Major, P0)
- [ ] **#24** [ALC-EP002-M09] Implement GET /health and GET /version (Major, P0)
- [ ] **#25** [ALC-EP002-m01] Parameterize thresholds via config (Minor, P1)
- [ ] **#26** [ALC-EP002-m02] Deterministic seeding/guards to reduce nondeterminism (Minor, P2)
- [ ] **#27** [ALC-EP002-m03] Validate image size against MAX_IMAGE_MB (Minor, P1)

**Progress**: 0/12 (0%) - Core feature implementation needed

### ALC-EP003: Functional Tests (P0) - 7 tasks
- [ ] **#28** [ALC-EP003-M01] Set up PyTest + Playwright API client fixtures (Major, P0)
- [ ] **#29** [ALC-EP003-M02] Happy path test (Major, P0)
- [ ] **#30** [ALC-EP003-M03] Overlay validation test (Major, P1)
- [ ] **#31** [ALC-EP003-M04] No-markings scenario test (Major, P1)
- [ ] **#32** [ALC-EP003-M05] JSON schema/contract validation (Major, P0)
- [ ] **#33** [ALC-EP003-m01] Test data utilities and fixtures for images (Minor, P2)
- [ ] **#34** [ALC-EP003-m02] Allure annotations and attachments (Minor, P2)

**Progress**: 0/7 (0%) - Test infrastructure needed

### ALC-EP004: Negative + Edge Tests (P1) - 5 tasks
- [ ] **#35** [ALC-EP004-M01] Negative: missing input, corrupt bytes, invalid params (Major, P1)
- [ ] **#36** [ALC-EP004-M02] Negative: oversized file (MAX_IMAGE_MB) (Major, P1)
- [ ] **#37** [ALC-EP004-M03] Edge: small/large, grayscale, night, extreme aspect ratios (Major, P1)
- [ ] **#38** [ALC-EP004-M04] Fuzz: invalid strings/URLs with Faker (Major, P2)
- [ ] **#39** [ALC-EP004-m01] Validate error shapes and messages (Minor, P2)

**Progress**: 0/5 (0%) - Error handling and edge case testing needed

### ALC-EP005: Performance Checks (P1) - 3 tasks
- [ ] **#40** [ALC-EP005-M01] Latency p95 threshold on /lanes (Major, P1)
- [ ] **#41** [ALC-EP005-M02] Stability: repeatability without memory bloat (Major, P2)
- [ ] **#42** [ALC-EP005-m01] Payload size checks (Minor, P2)

**Progress**: 0/3 (0%) - Performance validation needed

### ALC-EP006: CI/CD Pipelines + Reporting (P0) - 10 tasks
- [ ] **#43** [ALC-EP006-M01] Workflow: Lint & Security (Major, P0)
- [ ] **#44** [ALC-EP006-M02] Workflow: Unit tests (Major, P1)
- [ ] **#45** [ALC-EP006-M03] Workflow: API tests (functional + negative) on PRs (Major, P0)
- [ ] **#46** [ALC-EP006-M04] Workflow: Extended tests on main (Major, P1)
- [ ] **#47** [ALC-EP006-M05] Workflow: Allure reporting (Major, P1)
- [ ] **#48** [ALC-EP006-M06] Workflow: Docs deploy to GitHub Pages (Major, P1)
- [ ] **#49** [ALC-EP006-M07] Configure required checks: lint + functional (Major, P0)
- [ ] **#50** [ALC-EP006-m01] Cache pip and Docker layers (Minor, P2)
- [ ] **#51** [ALC-EP006-m02] Makefile targets used in CI jobs for parity (Minor, P2)

**Progress**: 0/10 (0%) - CI/CD infrastructure needed

### ALC-EP007: Docs Polish + Public Showcase (P2) - 6 tasks
- [ ] **#52** [ALC-EP007-M01] Finalize docs alignment (Major, P2)
- [ ] **#53** [ALC-EP007-M02] README: overview, badges, links (Major, P2)
- [ ] **#54** [ALC-EP007-M03] Publish docs and Allure to GitHub Pages (Major, P2)
- [ ] **#55** [ALC-EP007-m01] Add screenshots/diagrams (pipeline, ROI, overlays) (Minor, P3)
- [ ] **#56** [ALC-EP007-m02] Release notes / changelog entry (Minor, P3)

**Progress**: 0/6 (0%) - Documentation finalization needed

## Priority Breakdown

### P0 (Critical) - 15 tasks
- Foundation: 5 tasks
- Lane Detection: 5 tasks  
- Functional Tests: 3 tasks
- CI/CD: 2 tasks

### P1 (High) - 18 tasks
- Lane Detection: 2 tasks
- Functional Tests: 2 tasks
- Negative/Edge Tests: 3 tasks
- Performance: 1 task
- CI/CD: 6 tasks
- Docs: 4 tasks

### P2 (Medium) - 20 tasks
- Foundation: 3 tasks
- Lane Detection: 1 task
- Functional Tests: 2 tasks
- Negative/Edge Tests: 1 task
- Performance: 1 task
- CI/CD: 2 tasks
- Docs: 2 tasks

### P3 (Low) - 3 tasks
- Docs: 3 tasks

## Next Steps

### Immediate (P0 Priority)
1. **Foundation (#8-#12)**: Set up project structure, FastAPI app, Docker
2. **Lane Detection Core (#16-#20)**: Implement OpenCV pipeline and metrics
3. **Functional Tests (#28-#29)**: Set up test infrastructure and happy path

### Short Term (P1 Priority)
1. **API Endpoints (#22-#24)**: Implement schemas and routes
2. **CI Basics (#43, #45, #49)**: Lint, security, and required checks
3. **Test Coverage (#30-#31, #35-#37)**: Overlay, no-markings, and negative tests

### Medium Term (P2 Priority)
1. **Performance (#40-#42)**: Latency and stability validation
2. **CI Enhancement (#44, #46-#48)**: Unit tests, extended tests, reporting
3. **Documentation (#52-#54)**: Align docs and prepare for publication

## Workflow

- **Daily**: Update issue descriptions and checklists as progress changes
- **Weekly**: Triage new issues, adjust priorities, plan next milestones
- **At Merge**: Ensure PRs link to issues; let merge auto-close
- **Sprint End**: Review progress, update this tracking document

## Notes

- All issues are properly labeled with `type:epic|major|minor` and `priority:P0|P1|P2|P3`
- Each task links to its epic via the `epic:ALC-EP00X` label
- Issues follow the naming convention from `docs/TASKS.md`
- Use GitHub's saved searches for filtering:
  - P0 open: `is:issue is:open label:"priority:P0"`
  - My tasks: `is:issue is:open assignee:@me`
  - By epic: `is:issue is:open label:"epic:ALC-EP001"`

---
*Last Updated: 2025-08-26*
*Total Issues: 56*
*Overall Progress: 7/56 (12.5%)*
