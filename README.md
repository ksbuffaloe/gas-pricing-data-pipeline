# Gas Pricing Data Pipeline

This project pulls weekly U.S. gas price data from the [EIA Open Data API](https://www.eia.gov/opendata/), stores it in a PostgreSQL database (running in Docker), and sets you up to build an updating dashboard.

---

## 📦 Tech stack

- Python (`requests`, `pandas`, `sqlalchemy`, `dotenv`)
- PostgreSQL (Docker container)
- Docker Compose
- `.env` for managing secrets
- [EIA Open Data API](https://www.eia.gov/opendata/)

---

## 🚀 How to run it

### 1️⃣ Clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/gas-pricing-data-pipeline.git
cd gas-pricing-data-pipeline
