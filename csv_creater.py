import pandas as pd

# This data simulates real internal feedback for the Digital Accelerator team
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'date': ['2026-01-05', '2026-01-06', '2026-01-07', '2026-01-08', 
             '2026-01-09', '2026-01-10', '2026-01-11', '2026-01-12'],
    'feedback_text': [
        "The new AI auditing tool is saving us hours of manual work. Great job!",
        "The dashboard is a bit slow when loading large PDFs. Needs optimization.",
        "I am confused by the new login process. It takes too many steps.",
        "Excellent support from the Digital Accelerator team on the Azure setup.",
        "The documentation for the Python scripts is missing some key details.",
        "Pricing for the new service is too high compared to last year.",
        "The Power BI visualization is very clear and easy to understand.",
        "We need more research on Generative AI automation for the legal team."
    ]
}

df = pd.DataFrame(data)
df.to_csv('feedback_data.csv', index=False)
print("✅ feedback_data.csv has been created successfully!")