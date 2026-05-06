FROM odoo:16.0

# Switch to root to change permissions or install dependencies if needed
USER root

# Copy custom addons
COPY ./custom_addons /mnt/extra-addons/

# Ensure proper permissions
RUN chown -R odoo:odoo /mnt/extra-addons

# Switch back to odoo user
USER odoo
