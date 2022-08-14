import pandas as pd
import numpy as np

from pandas.api.types import CategoricalDtype
df = pd.DataFrame({"A": np.arange(6), "B": list("aabbca")})

df["B"] = df["B"].astype(CategoricalDtype(list("cab")))

print(df)
print()

print(df.dtypes)
print()

print(df["B"].cat.categories)

df2 = df.set_index("B")

print(df2.index)

print(df2.loc["a"])


print(df2.loc["a"].index)

print()
print(df2.sort_index())


print(df2.groupby(level=0).sum())

print()

print(df2.groupby(level=0).sum().index)
print()


df3 = pd.DataFrame(
    {"A": np.arange(3), "B": pd.Series(list("abc")).astype("category")}
)

df3 = df3.set_index("B")
print(df3)


print(df3.reindex(["a", "e"]).index)

print()

print(df3.reindex(pd.Categorical(["a", "e"], categories=list("abe"))))

print(df3.reindex(pd.Categorical(["a", "e"], categories=list("abe"))).index)

print()

indexf = pd.Index([1.5, 2, 3, 4.5, 5])

print(indexf)

sf = pd.Series(range(5), index=indexf)

print(sf)

print()

sf[3]

print(sf[3])

print()


print(sf[3.0])

print()


sf.loc[3]

print(sf.loc[3])

print(sf.loc[3.0])

print()

print(sf.loc[3.0])


print()


print(sf.iloc[3])

print()


print(sf[2:4])


print(sf.loc[2:4])


print()

print(sf.iloc[2:4])

print()

print(sf[2.1:4.6])

print()

dfir = pd.concat(
    [
        pd.DataFrame(np.random.randn(5,2), index=np.arange(5) * 250.0, columns =list("AB")),
        pd.DataFrame(
            np.random.randn(6, 2), index=np.arange(4, 10) * 250.1, columns =list("AB")
        ),
    ]
)

print()


print(dfir)

print()

print(dfir[0:1000.4])

print()

print(dfir.loc[0:1001, "A"])

print()

print(dfir[0:1000])

print()

print(dfir.iloc[0:5])

print()


df = pd.DataFrame(
    {"A": [1, 2, 3, 4]}, index=pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4])
)

print(df)

print()

print(df.loc[2])

print()

print(df.loc[[2, 3]])

print()

print(df.loc[2.5])

print()

print(df.loc[[2.5, 3.5]])

print()

print(df.loc[pd.Interval(1, 2)])

print()

idxr = df.index.overlaps(pd.Interval(0.5 ,2.5))

print(idxr)

print()

print(df[idxr])

print()

c = pd.cut(range(4), bins = 2)

print(c)

print()

print(c.categories)

print()

print(pd.cut([0, 3, 5, 1], bins = c.categories))

print()


print()


#generating ranges of intervals

pd.interval_range(start=0, end=5)
print(pd.interval_range(start =0, end=5))

print()

pd.interval_range(start = pd.Timestamp("2017-01-01"), periods =4)

print(pd.interval_range(start = pd.Timestamp ("2022-07-23 "), periods = 4))



print()

pd.interval_range(end = pd.Timedelta("3 days"), periods =4)
print(pd.interval_range(end= pd.Timedelta("4 days"), periods =4))


print()


print(pd.interval_range(start = 0, periods = 5, freq = 1.5))

print()


print(pd.interval_range(start = pd.Timestamp("2022-07-23"), periods= 4, freq="9H"))

print()



pd.interval_range(start = 0, end=4, closed="both")

print(pd.interval_range(start=0, end =4 , closed="both"))

print()


pd.interval_range(start=0,end=4, closed="both")

print(pd.interval_range(start=0, end=4, closed="both"))
print()



print(pd.interval_range(pd.Timestamp("2022-06-01"), pd.Timestamp("2022-07-01"),periods = 3))

print()

s = pd.Series(range(5))


print(s)


print()

df = pd.DataFrame(np.random.randn(5, 4))

print(df)
print()

print(df.loc[-2:])

print()


df = pd.DataFrame(index=[2, 3, 3, 4, 5], columns=["data"], data=list(range(5)))


print(df)

print()

df = pd.DataFrame(index= [2, 3, 3, 4, 5] , columns =["data"], data =list(range(5)))

print()


print(df)

print(df.index.is_monotonic_decreasing)

print()


print(df.loc[0:4, :])


print()


print(df.loc[13:15, :])


print()


df = pd.DataFrame(index=[2, 3, 1, 4, 3, 5] , columns=["data"], data=list(range(6)))


print(df)


print()

print(df.index.is_monotonic_increasing)

print()

print(df.loc[2:4, :])

print()

#keyError
#print(df.loc[0:4, :])

# 3 is not a unique label
#print()
#print(df.loc[2: 3, :])

print()


weakly_monotonic = pd.Index(["a", "b", "c", "c"])

print(weakly_monotonic.is_monotonic_increasing)

print()


print(weakly_monotonic)

print()


print(weakly_monotonic.is_monotonic_increasing & weakly_monotonic.is_unique)

print()


s = pd.Series(np.random.randn(6), index=list("abcdef"))


print()


print(s)

print()


print(s[2: 5])


print()


series1 = pd.Series([1, 2, 3])


print(series1.dtype)

print()

res = series1.reindex([0, 4])

print(res)

print()

print(res.dtype)

print()

print(res)

print()

series2 = pd.Series([True])


print()

print(series2.dtype)

print()

res = series2.reindex_like(series1)

print(res.dtype)


print()
print(res)


print()


df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D4"]
    },
    index=[0, 1, 2, 3]
)

print()


print(df1)


print()



df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"]
    },
    index = [0, 1, 2, 3]
)


print()



print(df2)


print()


df3 = pd.DataFrame(
    {
        "A":["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"]
    },
    index = [0, 1, 2, 3]
)


print(df3)


print()


frames = [df1, df2, df3]


result = pd.concat(frames)

print()


print(result)


print()

frames1 = [df1,df2]

result = pd.concat(frames1)

print(result)


print()




# print(pd.concat(
#     result, 
#     axios=0,
#     join="outer",
#     ignore_index=False,
#     keys=None,
#     levels=None,
#     names=None,
#     verify_integrity=False,
#     copy=True
# ))



result = pd.concat(frames, keys=["x", "y", "z"])

print(result)

print()


print(result.loc["y"])

print()


df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B5", "B7"],
        "C": ["C2", "C3", "C6", "C7"],
        "D": ["D2", "D4", "D6", "D7"],
    },
    index=[2, 3, 6, 7]
)

result = pd.concat([df1, df4], axis= 1)

print(result)



print()

result = pd.concat([df1, df4], axis=1).reindex(df1.index)


print()


result = pd.concat([df1, df4], ignore_index=True, sort=False)

print()

s1 = pd.Series(["x0", "x1", "x2", "x3"], name="x")

print()

result = pd.concat([df1, s1], axis=1)

print()

s1 = pd.Series(["x0", "x1", "x2", "x3"], name="x")

print()

result = pd.concat([df1, s1], axis=1)

print()


s2 = pd.Series(["_0", "_1", "_2", "_3"])

print()

result = pd.concat([df1, s2, s2, s2], axis=1)

print()

result = pd.concat([df1, s1], axis=1, ignore_index=True)

print(result)

print()

s3 = pd.Series([0, 1, 2, 3], name="foo")
print()
print(s3)

s4 = pd.Series([0, 1, 2, 3])

print()

s5 = pd.Series([0, 1, 4, 5])

print()

pd.concat([s3, s4, s5], axis=1)


pd.concat([s3, s4, s5], axis=1 , keys=["red", "blue", "yellow"])


print()


result = pd.concat(frames, keys=["x", "y", "z"])

print(result)


pieces = {"x":df1, "y": df2, "z":df3}

print()

result = pd.concat(pieces)

result = pd.concat(pieces, keys=["z", "y"])

print()


print(result.index.levels)


print()


s2 = pd.Series(["x0", "x1", "x2", "x3"], index=["a", "b", "c", "d"])

print(s2)


print()


result = pd.concat([df1, s2.to_frame().T], ignore_index=True)


print(result)


print()


# pd.merge(
#     left,
#     right,
#     how="inner",
#     on=None,
#     left_on=None,
#     right_on=None,
#     left_index=False,
#     right_index=False,
#     sort=True,
#     suffixes=("_x", "_y"),
#     copy=True,
#     indicator=False,
#     validate=None,
# )

left = pd.DataFrame(
    {
        "key": ["k0", "k1", "k2", "k3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B":["B0", "B1", "B2", "B3"],
    }
)


right = pd.DataFrame(
    {
        "key": ["k0", "k1", "k2", "k3"],
        "C": ["C0","C1", "C2", "C3"],
        "D":["D0", "D1", "D2", "D3"]
    }
)


result = pd.merge(left, right, on="key")

print()


print(result)

print()

left = pd.DataFrame(
    {
        "key1": ["k0", "k1", "k2", "k3"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B":["B0", "B1", "B2", "B3"],
    }
)

right = pd.DataFrame(
    {
        "key1": ["k0", "k1", "k2", "k3"],
        "key2": ["K0", "K1", "K0", "K1"],
        "C": ["C0","C1", "C2", "C3"],
        "D":["D0", "D1", "D2", "D3"]
    }
)

print()


result2 = pd.merge(left, right, on=["key1", "key2"])


print(result2)


print()


print()


df = pd.DataFrame({"let": ["A", "B", "C"], "num": [1, 2, 3]})

print(df)

print()


ser = pd.Series(["a", "b", "c", "d", "e", "f"],
                index=pd.MultiIndex.from_arrays([["A", "B", "C"] *  2, 
                [1, 2, 3, 4, 5, 6]], names=["let", "num"]))


print()


print(ser)

print()

print()


print(pd.merge(df, ser.reset_index(), on=["let", "num"]))


print()

print()

left = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

print()

print(left)


right = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

print()

result = pd.merge(left, right, on="B", how="outer")


print()

left = pd.DataFrame({"A":[1, 2], "B": [3, 4]})

right = pd.DataFrame({"A": [3, 4], "B": [3, 4]})


print()

print(pd.merge(left, right, on="B", how="outer", validate="one_to_one"))

print()

print(pd.merge(left, right, on="B", how="outer", validate="one_to_many"))


print()

print()



# dataframes init

df1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

print()

print(df1)


df2 = pd.DataFrame({"col1": [1, 2], "col3": [3, 4]})

print(df2)

print()

result = pd.merge(df1, df2 , on="col1", how="outer", indicator=True)

print(result)

print()

left = pd.DataFrame({"key": [1], "v1": [10]})

print(left)
print()

right = pd.DataFrame({"key": [1, 2], "v1" :[20, 30]})

print(right)
print()

print(pd.merge(left, right, how="outer"))

print()

print(pd.merge(left, right, how="outer", on="key").dtypes)

print()

print()

from pandas.api.types import CategoricalDtype

x = pd.Series(np.random.choice(["foo", "bar"], size=(10, )))

print(x)

x = x.astype(CategoricalDtype(categories=["foo", "bar"]))

left = pd.DataFrame(
    {"x": x, "y": np.random.choice(["one", "two","three"], size=(10, ))}
)

print(left)

print()

print(left.dtypes)

print()


right = pd.DataFrame(
    {
        "x": pd.Series(["foo", "bar"], dtype=CategoricalDtype(["foo","bar"]))
    }
)


print(right)


print(right.dtypes)


print()


result = pd.merge(left, right, how="outer")

print(result)

print(result.dtypes)

print()



left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

print(left)

print()


right = pd.DataFrame(
    {"C":["C0", "C1", "C2"], "D": ["D0", "D1", "D2"]},index = ["K0", "K2", "K3"]
)


print(right)

result = left.join(right)
print()

print(result)

result = left.join(right, how="inner")

print()
    
print(result)

print()


result = pd.merge(left, right, left_index = True, right_index = True, how="outer")

print(result)


print()


result = pd.merge(left, right, left_index=True, right_index=True, how="inner")

print(result)

print()

