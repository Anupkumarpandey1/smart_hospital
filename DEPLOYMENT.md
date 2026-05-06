# 🚀 Step-by-Step Free Deployment Guide (Render)

This guide will walk you through deploying your Smart Hospital Management System on Render for **free**. We have already configured the infrastructure as code via the `render.yaml` and `Dockerfile` in your repository.

## Prerequisites
1. Your code must be pushed to a GitHub repository (which you've already done!).
2. A free account on [Render](https://render.com/).

---

## Deployment Steps

### Step 1: Create a Render Blueprint
1. Log in to your [Render Dashboard](https://dashboard.render.com/).
2. In the top right corner, click the **New +** button and select **Blueprint**.

### Step 2: Connect Your GitHub Repository
1. If you haven't already, authorize Render to access your GitHub repositories.
2. Search for your repository `smart_hospital` in the list and click **Connect**.

### Step 3: Apply the Blueprint
1. Render will automatically read the `render.yaml` file located in the root of your project.
2. It will recognize two services that need to be created:
   - **odoo-db**: A Free PostgreSQL Database.
   - **odoo-hospital-system**: A Free Docker Web Service.
3. Scroll down and click **Apply** or **Save**. 

Render will now start building your Odoo Docker image and provisioning the database. This process might take 5-10 minutes. 

### Step 4: Access Your Live Application
1. Go to your Render Dashboard and click on the **odoo-hospital-system** Web Service.
2. Once the deployment is marked as **Live** (green status), click on the URL provided just below the service name (e.g., `https://odoo-hospital-system-xxxxx.onrender.com`).
3. You will be greeted by the initial Odoo Database creation screen.

### Step 5: Configure the Odoo Database
1. **Master Password**: Keep the default or set a new one.
2. **Database Name**: Enter `odoo`.
3. **Email**: Enter your admin email (used for login).
4. **Password**: Enter your admin password.
5. **Language/Country**: Fill as desired.
6. **Demo Data**: Leave unchecked unless you want standard Odoo demo data.
7. Click **Create database**.

### Step 6: Install the Hospital Module
1. Once the database is created, you will be logged in as the admin. Go to the **Apps** menu.
2. In the search bar at the top, click the `X` next to the `Apps` filter to remove it.
3. Search for `Hospital Management System`.
4. Click the **Activate** button on your custom module.

🎉 **Congratulations! Your Smart Hospital Management System is now live on the internet!**

---

## ⚠️ Important Limitations of the Free Tier
* **Sleep Mode**: Render's free web services will spin down (go to sleep) after 15 minutes of inactivity. When you access the site again, it may take 1-2 minutes to "wake up" and load the page.
* **Database Expiration**: Render's free PostgreSQL databases expire and are automatically deleted after **90 days**. For a permanent portfolio project, you should regularly back up your database from the Odoo UI or upgrade the database to the cheapest paid tier.
