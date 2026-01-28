# Programming Languages and Versions

## Repository Overview
**Repository**: thevgergroup/flask-file-explorer
**Description**: A Flask-based file explorer with drag-and-drop upload capabilities
**Analysis Date**: 2026-01-25

---

## Primary Programming Languages

### Python
- **Version**: ^3.11 (Python 3.11+)
- **Purpose**: Backend web application framework
- **Configuration**: pyproject.toml:19
- **Usage**: Core application logic, Flask web server, file system operations

### JavaScript (ES6+)
- **Purpose**: Frontend interactivity and dynamic behavior
- **Files**:
  - flask_file_explorer/static/flask-file-explorer/js/script.js:1
- **Usage**: HTMX integration, Dropzone file upload handling, modal management, directory tree toggling

### HTML5
- **Purpose**: Web interface structure
- **Template Engine**: Jinja2 3.1.3
- **Files**:
  - flask_file_explorer/templates/flask-file-explorer/index.html:1
  - flask_file_explorer/templates/flask-file-explorer/listings.html
  - flask_file_explorer/templates/flask-file-explorer/modal.html
- **Usage**: File explorer interface, directory listings, file viewer modal

### CSS3
- **Purpose**: Styling and visual design
- **Files**: flask_file_explorer/static/flask-file-explorer/css/style.css
- **Usage**: Custom styling with gradient backgrounds, active directory highlighting

---

## Core Dependencies

### Python Backend Framework
| Package | Version | Purpose |
|---------|---------|---------|
| flask | 3.0.1 | Web application framework |
| Werkzeug | 3.0.1 | WSGI utility library (Flask dependency) |
| Jinja2 | 3.1.3 | Template engine for HTML rendering |
| click | 8.1.7 | Command-line interface toolkit (Flask dependency) |
| itsdangerous | 2.1.2 | Secure data signing (Flask dependency) |
| blinker | 1.7.0 | Signal/event handling (Flask dependency) |

### Development & Debugging Tools
| Package | Version | Purpose |
|---------|---------|---------|
| icecream | 2.1.3 | Enhanced debugging output tool |

### Python Support Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| asttokens | 2.4.1 | AST token annotation (icecream dependency) |
| executing | 2.0.1 | AST execution tracking (icecream dependency) |
| colorama | 0.4.6 | Cross-platform colored terminal output |
| MarkupSafe | 2.1.4 | String escaping (Jinja2 dependency) |

---

## Frontend Dependencies (CDN-based)

### JavaScript Libraries
| Library | Version | Purpose | Source |
|---------|---------|---------|--------|
| jQuery | 3.7.1 | DOM manipulation and AJAX | code.jquery.com |
| Bootstrap | 5.3.2 | UI framework and responsive design | cdn.jsdelivr.net |
| HTMX | latest | Dynamic HTML without JavaScript | cdn.jsdelivr.net |
| Dropzone.js | 5.9.3 | Drag-and-drop file upload | unpkg.com |

### CSS Frameworks & Icons
| Library | Version | Purpose | Source |
|---------|---------|---------|--------|
| Bootstrap CSS | 5.3.2 | UI styling | cdn.jsdelivr.net |
| Boxicons | 2.1.4 | Icon library | unpkg.com |
| Dropzone CSS | 5.x | File upload styling | unpkg.com |

---

## Build & Deployment Tools

### Package Management
- **Tool**: Poetry 1.7.1
- **Configuration**: pyproject.toml, poetry.lock
- **Purpose**: Python dependency management and packaging

### Dynamic Versioning
- **Tool**: poetry-dynamic-versioning (>=1.0.0, <2.0.0)
- **Configuration**: pyproject.toml:25-29
- **Purpose**: Automatic version management from git tags

### Build System
- **Build Backend**: poetry_dynamic_versioning.backend
- **Build Tool**: pypa/build
- **Output**: Binary wheel and source tarball
- **Configuration**: pyproject.toml:27-29

---

## CI/CD & Automation

### GitHub Actions Workflows
**File**: .github/workflows/python-publish.yml:1

#### Build Job
- **Runner**: ubuntu-latest
- **Python Version**: 3.x (latest)
- **Steps**:
  1. Checkout code (actions/checkout@v4)
  2. Setup Python (actions/setup-python@v4)
  3. Install build tools (pypa/build)
  4. Build distribution packages
  5. Upload artifacts (actions/upload-artifact@v3)

#### Publish Job
- **Trigger**: Git tag pushes (refs/tags/*)
- **Target**: PyPI (pypi.org/p/flask-file-explorer)
- **Authentication**: Trusted publishing (OIDC)
- **Action**: pypa/gh-action-pypi-publish@release/v1

### Dependency Management
**File**: .github/dependabot.yml:1
- **Ecosystem**: pip
- **Schedule**: Weekly updates
- **Directory**: / (root)

---

## Testing & Quality Assurance

### Test Framework
- **Status**: No test files found in repository
- **Test Directory**: Not present
- **Coverage**: None configured

### Code Quality Tools
- **Linting**: Not configured
- **Formatting**: Not configured
- **Type Checking**: Not configured

---

## Security Considerations

### Built-in Security Features
1. **Path Traversal Protection**:
   - All file paths verified against FFE_BASE_DIRECTORY
   - Absolute path validation (file_explorer.py:35)
2. **Authentication**: BYOA (Bring Your Own Authentication)
   - Example provided using Flask-Login
   - Blueprint-based request filtering

### Security Requirements
- **Python Version**: 3.11+ (receives security updates)
- **Flask Version**: 3.0.1 (latest stable)
- **Dependency Updates**: Weekly via Dependabot

---

## Development Environment

### Required Tools
1. **Python**: 3.11 or higher
2. **Poetry**: For dependency management
3. **Git**: For version control

### Optional Tools
1. **Flask-Login**: For authentication integration
2. **Docker**: For containerized deployments (mentioned in README)

### Environment Configuration
```python
# Required Flask configuration
app.config["FFE_BASE_DIRECTORY"] = 'path/to/directory'
```

---

## Deployment Targets

### Package Distribution
- **PyPI**: Official package repository
  - Package name: flask-file-explorer
  - URL: https://pypi.org/p/flask-file-explorer
  - Version: Dynamic (git-tag based)

### Installation Methods
```bash
# Poetry
poetry add flask-file-explorer

# pip
pip install flask-file-explorer

# Git source
poetry add git+https://github.com/thevgergroup/flask-file-explorer
```

### Runtime Requirements
- **WSGI Server**: Any WSGI-compatible server (e.g., Gunicorn, uWSGI)
- **Web Server**: Optional reverse proxy (e.g., Nginx, Apache)
- **Platform**: Linux, macOS, Windows (cross-platform)

---

## Version Compatibility Matrix

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| Python | 3.11 | 3.11+ | Required by pyproject.toml |
| Flask | 3.0.0 | 3.0.1+ | Core framework |
| Poetry | 1.0.0 | 1.7.1+ | Build system |
| Bootstrap | 5.3.2 | 5.3.2+ | Frontend framework |
| jQuery | 3.7.1 | 3.7.1+ | DOM manipulation |

---

## Notable Technology Choices

### Why These Technologies?

1. **Flask**: Lightweight, flexible web framework perfect for simple file explorer
2. **Poetry**: Modern Python package management with lock file support
3. **HTMX**: Dynamic updates without heavy JavaScript framework
4. **Dropzone.js**: Mature drag-and-drop file upload solution
5. **Bootstrap**: Rapid UI development with responsive design
6. **Jinja2**: Flask's default templating engine, familiar to developers

### Architecture Pattern
- **Blueprint-based**: Modular Flask design for easy integration
- **Template-driven**: Server-side rendering with HTMX for dynamic updates
- **CDN-based frontend**: No build step required for JavaScript/CSS

---

## License
- **Type**: MIT License
- **File**: LICENSE:1
- **Year**: Not specified in license file

---

## Summary

Flask-file-explorer is a modern Python 3.11+ web application built with Flask 3.0.1 and managed using Poetry. The frontend leverages Bootstrap 5.3.2, jQuery 3.7.1, HTMX, and Dropzone.js for a rich user experience without requiring a complex build process. The project uses GitHub Actions for automated building and publishing to PyPI, with Dependabot providing weekly dependency updates. No testing framework is currently configured.
