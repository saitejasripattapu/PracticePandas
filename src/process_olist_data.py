"""Read all five Olist CSVs and save separate outputs.

No rows are removed or missing values filled. Add cleaning steps only after
recording and justifying them in docs/observation.md.
"""

from pathlib import Path

import pandas as pd


def main():
    project_root = Path(__file__).resolve().parent.parent
    raw_directory = project_root / "data" / "raw"
    processed_directory = project_root / "data" / "processed"
    processed_directory.mkdir(parents=True, exist_ok=True)

    dataset_names = [
        "orders",
        "customers",
        "order_items",
        "products",
        "order_reviews",
    ]

    # Read and save every dataset in the list.
    for name in dataset_names:
        print(f"Processing dataset: {name}")
        input_path = raw_directory / f"olist_{name}_dataset.csv"
        output_path = processed_directory / f"{name}.csv"

        # Preserve ZIP-code text, including leading zeros, as supplied.
        # This condition controls column types, not which files are processed.
        column_types = (
            {"customer_zip_code_prefix": "string"}
            if name == "customers" else None
        )
        dataframe = pd.read_csv(input_path, dtype=column_types)

        # Add transformations here once your observations justify them.
        dataframe.to_csv(output_path, index=False)

        rows, columns = dataframe.shape
        print(
            f"Saved {output_path.relative_to(project_root)}: "
            f"{rows:,} rows, {columns} columns"
        )

    print(f"Finished processing all {len(dataset_names)} datasets.")


if __name__ == "__main__":
    main()
