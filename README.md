# Business Intelligence Application (Bug Hunt & Bug Report)

This is a simple Business Intelligence application built with Flask and Bootstrap, designed for an educational activity focused on bug hunting and reporting. The application intentionally contains several bugs for students to identify, reproduce, and document.

## Installation and Setup

1.  **Clone the repository (or download the files):**

    ```bash
    git clone https://github.com/gdbarros94/effective-eureka
    cd bi_app
    ```

    (Note: Since this is a direct file delivery, you would typically provide a zip file or similar for students to download and extract.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install Flask Chart.js
    ```
    (Note: Chart.js is included via CDN in `base.html`, so it's not a direct Python dependency, but Flask is.)

4.  **Run the application:**

    ```bash
    python3 app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`.

## Application Overview

The application has three main sections:

*   **Dashboard:** Displays a bar chart of monthly sales and includes data filtering and search functionalities.
*   **KPI Calculation:** Allows users to calculate ROI and Margin based on input revenue and cost.
*   **Navigation Menu:** Provides links to switch between the Dashboard and KPI Calculation sections.

## Intentional Bugs (for Bug Hunt Activity)

This application contains several deliberate bugs, categorized as subjective/business logic bugs and clear/implementation bugs. Your task is to find them, reproduce them, and document their behavior.

### A) Subjective / Business Logic Bugs

1.  **Incorrect ROI Formula:**
    *   **Description:** The Return on Investment (ROI) calculation uses an incorrect formula, leading to misleading results.
    *   **Reproduction Steps:**
        1.  Navigate to the "KPIs" section (or attempt to).
        2.  Enter values for "Receita" (Revenue) and "Custo" (Cost) in the KPI Calculation form.
        3.  Click "Calcular" (Calculate).
        4.  Observe the calculated ROI. Compare it with the correct formula: `(Revenue - Cost) / Revenue * 100`.

2.  **Swapped Sales Chart Axes:**
    *   **Description:** On the Dashboard, the monthly sales bar chart displays the X and Y axes inverted. Months appear on the Y-axis, and sales values appear on the X-axis.
    *   **Reproduction Steps:**
        1.  Navigate to the "Dashboard" section.
        2.  Observe the "Vendas Mensais" (Monthly Sales) bar chart.
        3.  Notice that the labels for months are on the Y-axis and the sales values are on the X-axis, which is counter-intuitive for a typical bar chart of this type.

3.  **"KPIs" Menu Button Redirects to Dashboard:**
    *   **Description:** The "KPIs" button in the navigation menu incorrectly redirects the user to the Dashboard page instead of the KPI Calculation page.
    *   **Reproduction Steps:**
        1.  Click on the "KPIs" link in the top navigation bar.
        2.  Observe that you are redirected to the Dashboard page instead of the expected KPI Calculation page.

### B) Clear / Implementation Bugs

4.  **Infinite Loop on Data Filter (Month 13):**
    *   **Description:** If the user attempts to filter data by entering the month "13" (an invalid month number), the application enters an infinite loop, causing it to become unresponsive.
    *   **Reproduction Steps:**
        1.  Navigate to the "Dashboard" section.
        2.  Locate the "Filtrar Dados" (Filter Data) section.
        3.  In the "Mês" (Month) input field, enter `13`.
        4.  Click "Filtrar" (Filter).
        5.  Observe that the application becomes unresponsive (e.g., the browser tab might freeze or show a 


loading spinner indefinitely), and you might need to restart the Flask server.

5.  **Export Button Not Displaying:**
    *   **Description:** The "Exportar" (Export) button, intended to appear only for admin users, never displays because the `user.is_admin` variable is never correctly set to `True` within the application's logic.
    *   **Reproduction Steps:**
        1.  Navigate to the "Dashboard" section.
        2.  Observe that there is no "Exportar" button visible, even though the code intends for it to be conditionally displayed.
        3.  (For advanced users/inspecting code): Examine `app.py` and `dashboard.html` to see how `user.is_admin` is handled.

6.  **Search Field Unresponsive (Console Error):**
    *   **Description:** The search input field on the Dashboard does not respond to user input as expected, and an error related to an undefined function appears in the browser's developer console.
    *   **Reproduction Steps:**
        1.  Navigate to the "Dashboard" section.
        2.  Locate the "Buscar Dados" (Search Data) section.
        3.  Open your browser's developer console (usually by pressing F12).
        4.  Type something into the "Termo de Busca" (Search Term) input field.
        5.  Observe that no immediate action occurs, and an error message (e.g., "some_non_existent_function is not defined") appears in the browser's console.


