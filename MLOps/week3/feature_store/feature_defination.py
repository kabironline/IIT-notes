import os
from datetime import timedelta

from feast import Entity, FeatureView, Field
from feast.infra.offline_stores.bigquery import BigQuerySource
from feast.value_type import ValueType
from feast.types import Float32, Int64, String

iris = Entity(
    name="iris_id",
    description="The unique identifier for an iris specimen or observation group.",
    value_type=ValueType.INT64, 
)

# Configuration updated with your PROJECT_ID
iris_data_source = BigQuerySource(
    name="iris_data_bigquery_source",
    table="mystical-atlas-473806-i7.feast_datasets.iris_measurements",
    timestamp_field="event_timestamp",
)

iris_features = FeatureView(
    name="iris_measurements_v1",
    entities=[iris],
    ttl=timedelta(days=1), 
    
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="species", dtype=String),
    ],
    source=iris_data_source,
    tags={"source_data": "iris_dataset"},
)
