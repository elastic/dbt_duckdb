# SQL Test dbt Project

Welcome to the sql test repository! This project is based on the [dbt](https://www.getdbt.com/) and uses an embedded [DuckDB](https://duckdb.org/) database with sample Salesforce data.

The goal of this test is to evaluate your understanding of SQL, dbt, and dimensional data modeling concepts.

## Instructions

- **Fork the Repository**
- **Clone Your Fork**
- **Set Up dbt**
- **Explore Staging Models**
- **Build Dimension & Fact Models**:  
   Based on the relevant staging models, create the following:
   - **Dimension Models**: Identify and create necessary dimension tables. These can be date dimensions, user dimensions, product dimensions, etc. depending on the staging data provided.
   - **Fact Models**: Build out the fact tables that centralize the measures and keys.
   
   Ensure your models are placed in the appropriate directories (e.g., `models/dimensions/` and `models/facts/`).

6. **Test Your Models**:  
   Use dbt's testing functionality to ensure the integrity of your models. Ensure that relationships are correctly established, and there are no data anomalies.
   ```bash
   dbt run
   dbt test
   ```

7. **Commit Your Changes**:  
   Once you're satisfied with your models, commit your changes:
   ```bash
   git add .
   git commit -m "Completed dimension and fact models"
   ```

8. **Push & Create Pull Request**:  
   Push your changes to your fork and then create a pull request against the original repository.
   ```bash
   git push origin main
   ```

9. **Submit Your Test**:  
   After creating the pull request, notify the hiring team or submit the link as per the application instructions.

## Evaluation

Your submission will be evaluated based on:

- Correctness of the models.
- Efficiency and simplicity of the SQL written.
- Adherence to dbt best practices.
- Robustness of tests and validations.

## Questions

If you have any questions or run into issues, please reach out to [contact@example.com](mailto:contact@example.com).

Best of luck, and we look forward to reviewing your models!

---

Adjust the content as needed based on the specifics of your test or any additional details you'd like to include.