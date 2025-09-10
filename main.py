from src.data_generator import DataGenerator
from src.etl_pipeline import run_etl
from src.doc_generator import generate_docs
from src.metadata_enricher import enrich_metadata
from src.optimizer import optimize_pipeline

def demo():
    print("🔹 Step 1: Generate Synthetic Data")
    path, df = DataGenerator().generate_employees(50)

    print("🔹 Step 2: Run ETL Pipeline")
    processed, db = run_etl(path)

    print("🔹 Step 3: Generate AI Documentation")
    doc_path = generate_docs("src/etl_pipeline.py")

    print("🔹 Step 4: Enrich Metadata")
    meta_path = enrich_metadata(processed)

    print("🔹 Step 5: Optimization Suggestions")
    opt_path = optimize_pipeline("src/etl_pipeline.py")

    print("\n✅ Demo complete!")
    print(f"Generated files:\n- {processed}\n- {doc_path}\n- {meta_path}\n- {opt_path}\n- {db}")

if __name__ == "__main__":
    demo()
