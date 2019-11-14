from finstmt.items.config import ItemConfig

# TODO: use regex instead of names list

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
INCOME_STATEMENT_INPUT_ITEMS = [
    ItemConfig(
        'revenue',
        'Revenue',
        extract_names=[
            'total revenue',
            'total rev',
            'total sales',
            'total sale',
            'revenue',
            'rev',
            'sales',
            'sale'
        ],
    ),
    ItemConfig(
        'cogs',
        'Cost of Goods Sold',
        extract_names=[
            'cost of revenue',
            'cost of goods sold',
            'cogs',
            'cor'
        ],
    ),
    ItemConfig(
        'gross_profit',
        'Gross Profit',
    ),
    ItemConfig(
        'rd_exp',
        'R&D Expense',
        extract_names=[
            'rd expenses',
            'rd expense',
            'rd exp',
            'rd',
            'research and development expenses',
            'research and development expense',
            'research and development exp',
            'research and development',
        ],
    ),
    ItemConfig(
        'sga',
        'SG&A Expense',
         extract_names=[
            'sga',
            'sga expense',
            'sga expenses',
            'sga exp',
            'selling general and administrative',
            'selling general and administrative expense',
            'selling general and administrative expenses',
            'selling general and administrative exp',
            'selling general administrative',
            'selling general administrative expense',
            'selling general administrative expenses',
            'selling general administrative exp',
            'selling general and admin',
            'selling general and admin expense',
            'selling general and admin expenses',
            'selling general and admin exp',
            'selling general admin',
            'selling general admin expense',
            'selling general admin expenses',
            'selling general admin exp',
        ],
    ),
    ItemConfig(
        'dep_exp',
        'Depreciation & Amortization Expense',
        extract_names=[
            'da',
            'dep amort',
            'dep and amort',
            'dep',
            'depreciation amort',
            'depreciation and amort',
            'depreciation',
            'depreciation amortization',
            'depreciation and amortization',
            'dep amortization',
            'dep and amortization',
        ]
    ),
    ItemConfig(
        'other_op_exp',
        'Other Operating Expenses',
        extract_names=[
            'other operating expenses',
            'other operating expense',
            'other operating exp',
            'other op expenses',
            'other op expense',
            'other op exp',
            'other operating expensesincome',
            'other operating expenseincome',
            'other operating expincome',
            'other op expensesincome',
            'other op expenseincome',
            'other op expincome',
            'other operating expenses income',
            'other operating expense income',
            'other operating exp income',
            'other op expenses income',
            'other op expense income',
            'other op exp income',
            'other operating expensesinc',
            'other operating expenseinc',
            'other operating expinc',
            'other op expensesinc',
            'other op expenseinc',
            'other op expinc',
            'other operating expenses inc',
            'other operating expense inc',
            'other operating exp inc',
            'other op expenses inc',
            'other op expense inc',
            'other op exp inc',
        ]
    ),
    ItemConfig(
        'op_exp',
        'Operating Expense',
        extract_names=[
            'op expense',
            'op expenses',
            'op exp',
            'operating expense',
            'operating expenses',
            'operating exp',
        ],
    ),
    ItemConfig(
        'ebit',
        'Earnings Before Interest and Taxes',
        extract_names=[
            'ebit',
            'earnings before interest and taxes',
            'earnings before int and taxes',
            'earnings before interest and tax',
            'earnings before int and tax',
            'earn before interest and taxes',
            'earn before int and taxes',
            'earn before interest and tax',
            'earn before int and tax',
            'earnings before interest taxes',
            'earnings before int taxes',
            'earnings before interest tax',
            'earnings before int tax',
            'earn before interest taxes',
            'earn before int taxes',
            'earn before interest tax',
            'earn before int tax',
            'operating income',
            'op income',
            'op inc',
            'operating inc'
        ]
    ),
    ItemConfig(
        'int_exp',
        'Interest Expense',
        extract_names=[
            'int',
            'int expense',
            'int expenses',
            'int exp',
            'interest',
            'interest expense',
            'interest expenses',
            'interest exp',
        ],
    ),
    ItemConfig(
        'gain_on_sale_invest',
        'Gain on Sale of Investments',
        extract_names=[
            'gain loss on sale of invest',
            'gain loss sale of invest',
            'gain loss sale invest',
            'gain on sale of invest',
            'gain sale of invest',
            'gain sale invest',
            'gain loss on sale of investments',
            'gain loss sale of investments',
            'gain loss sale investments',
            'gain on sale of investments',
            'gain sale of investments',
            'gain sale investments',
        ]
    ),
    ItemConfig(
        'gain_on_sale_asset',
        'Gain on Sale of Assets',
        extract_names=[
            'gain loss on sale of assets',
            'gain loss sale of assets',
            'gain loss sale assets',
            'gain on sale of assets',
            'gain sale of assets',
            'gain sale assets',
            'gain loss on sale of asset',
            'gain loss sale of asset',
            'gain loss sale asset',
            'gain on sale of asset',
            'gain sale of asset',
            'gain sale asset',
        ]
    ),
    ItemConfig(
        'impairment',
        'Impairment Expense',
        extract_names=[
            'impairment',
            'impairment expense',
            'impairment exp',
            'impairments',
            'impair',
            'impair expense',
            'impair exp',
            'impairment charges',
            'impairment charge',
            'impair charges',
            'impair charge',
            'asset writedown',
            'assets writedown',
            'asset write down',
            'assets write down',
        ]
    ),
    ItemConfig(
        'ebt',
        'Earnings Before Tax',
        extract_names=[
            'ebt',
            'earnings before taxes',
            'earnings before tax',
            'earn before tax',
            'earn before taxes',
            'ebt including unusual items',
            'earnings before taxes including unusual items',
            'earnings before tax including unusual items',
            'earn before tax including unusual items',
            'earn before taxes including unusual items',
            'ebt inc unusual items',
            'earnings before taxes inc unusual items',
            'earnings before tax inc unusual items',
            'earn before tax inc unusual items',
            'earn before taxes inc unusual items',
            'ebt incl unusual items',
            'earnings before taxes incl unusual items',
            'earnings before tax incl unusual items',
            'earn before tax incl unusual items',
            'earn before taxes incl unusual items',
        ]
    ),
    ItemConfig(
        'tax_exp',
        'Income Tax Expense',
        extract_names=[
            'taxes',
            'tax',
            'tax expense',
            'tax expenses',
            'tax exp',
            'income tax',
            'income tax expense',
            'income tax expenses',
            'income tax exp',
        ],
    ),
    ItemConfig(
        'net_income',
        'Net Income',
        extract_names=[
            'net income',
            'net inc',
            'earnings',
            'earn',
        ]
    ),
]