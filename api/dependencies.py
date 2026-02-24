"""
Reusable dependencies
"""

from api.auth import require_role

doctor_only = require_role("DOCTOR")
admin_only = require_role("ADMIN")
