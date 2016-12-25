import numpy as np
import QuantLib as ql

# Set Evaluation Date
today = ql.Date(31,3,2015)
ql.Settings.instance().setEvaluationDate(today)

swapQuotes = \
[
    ql.SimpleQuote(0.03),
    ql.SimpleQuote(0.035)
]

swapTerms = \
[
    ql.Period(1, ql.Years),
    ql.Period(2, ql.Years),
    ql.Period(3, ql.Years),
    ql.Period(4, ql.Years),
    ql.Period(5, ql.Years)
]

swapHandles = map(lambda x: ql.QuoteHandle(x), swapQuotes)

# Setup the yield termstructure
disc_curve = ql.FlatForward(today, handles[0], ql.Actual365Fixed())
disc_curve.enableExtrapolation()
yts = ql.YieldTermStructureHandle(disc_curve)