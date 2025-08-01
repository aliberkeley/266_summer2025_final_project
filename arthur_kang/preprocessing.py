import pandas as pd

logic_climate_test = (
    pd.read_csv('climate_test_with_lst.csv')
      .dropna(subset=['source_article', 'logical_fallacies'])
)

logic_climate_test['logical_fallacies'] = (
    logic_climate_test['logical_fallacies']
    .replace('intentional', 'intentional fallacy')
)

logic_climate_test = logic_climate_test[
    logic_climate_test['logical_fallacies'] != 'equivocation'
]

logic_climate_test.loc[:, 'logical_fallacies'] = (
    logic_climate_test['logical_fallacies']
    .replace('fallacy of logic', 'deductive fallacy')
)

logic_climate_test.to_csv('climate_test_with_lst_cleaned.csv', index=False)
