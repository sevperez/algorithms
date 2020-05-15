import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

class AsymptoticAnalyzer:
    def range_list(self, n):
        """
        - Parameters: n (int).
        - Returns a list from 0...n.
        """
        return list(range(n + 1))

    def constant(self, n, c=10):
        """
        - Parameters: n (int), c (int) (default=10).
        - Returns a list of length n where all elements are c.
        """
        return [c for i in self.range_list(n)]

    def linear(self, n, c=1):
        """
        - Parameters: n (int), c (int) (default=1).
        - Returns a list of integers from 0...n, multiplied by
          the provided constant.
        """
        return [c * i for i in self.range_list(n)]

    def logarithmic(self, n, c=1):
        """
        - Parameters: n (int), c (int) (default=1).
        - Returns a list of c * log(i) for each i in 0...n.
        """
        logs = [c * math.log(i) for i in self.range_list(n)[1:]]
        logs = [0] + logs
        return logs

    def linearithmic(self, n, c=1):
        """
        - Parameters: n (int), c (int) (default=1).
        - Returns a list of c * i * log(i) for each i in 0...n.
        """
        lin_logs = [c * i * math.log(i) for i in self.range_list(n)[1:]]
        lin_logs = [0] + lin_logs
        return lin_logs

    def quadratic(self, n, c=1):
        """
        - Parameters: n (int), c (int) (default=1).
        - Returns a list of c * i^2 for each i in 0...n.
        """
        return [c * i**2 for i in self.range_list(n)]

    def polynomial(self, n, exp=3, c=1):
        """
        - Parameters: n (int), exp (int) (default=3), 
          c (int) (default=1).
        - Returns a list of c * i^exp for each i in 0...n.
        """
        return [c * i**exp for i in self.range_list(n)]

    def exponential(self, n, base=2, c=1):
        """
        - Parameters: n (int), base (int) (default=2), 
          c (int) (default=1).
        - Returns a list of c * base^i for each i in 0...n.
        """
        return [c * base**i for i in self.range_list(n)]

    def factorial(self, n, c=1):
        """
        - Parameters: n (int), c (int) (default=1).
        - Returns a list of c * i! for each i in 0...n.
        """
        return [c * math.factorial(i) for i in self.range_list(n)]

    def calculate(self, n, coefficients):
        """
        - Parameters: n (int), coefficients (list of reals).
        - Returns a list of length n with results of the formula.
            - Iterates from 0...n (i)
            - Iterates through coefficients (c) by index (exp)
            - Results are calculated as c * (i^exp)
            - For example, the call equation([3, 4, 5, 6])
              returns the results from 0...n of the formula
              3 + 4i + 5i^2 + 6i^3.
        """
        results = []
        for i in self.range_list(n):
            current = 0
            for exp, c in enumerate(coefficients):
                current += c * (i**exp)
            results.append(current)
        return results

    def growth_rate_df(self, n, c_cons=10, c_poly=3, c_exp=2):
        """
        - Parameters: n (int), c_cons (int) (default=10), 
          c_poly (int) (default=3), c_exp (int) (default=2).
        - Returns a Pandas dataframe of n observations with columns
          for each of the common growth rates. Provided constants are
          used in corresponding growth rates.
        """
        df = pd.DataFrame({"n": [i for i in self.range_list(n)]})
        df["constant"] = self.constant(n, c_cons)
        df["linear"] = self.linear(n)
        df["linearithmic"] = self.linearithmic(n)
        df["quadratic"] = self.quadratic(n)
        df["polynomial"] = self.polynomial(n, c_poly)
        df["exponential"] = self.exponential(n, c_exp)
        df["factorial"] = self.factorial(n)
        return df

    def rate_comparison_df(self, n, rate_dictionary):
        """
        - Parameters: n (int), rate_dictionary.
        - Returns a Pandas dataframe comprised of the input values of
          rate_dictionary.
        """
        df = pd.DataFrame({"n": [i for i in self.range_list(n)]})
        for key in rate_dictionary.keys():
            df[key] = rate_dictionary[key]
        return df

    def convert_to_long(self, df):
        """
        - Parameters: df (Pandas dataframe).
        - Returns the provided dataframe in long format, including
          variables "n", "rate", and "value". Assumes that the dataframe
          has an id variable "n"
        """
        long_df = df.melt(id_vars="n", var_name="rate",
                          value_name="value")
        long_df["value"] = long_df["value"].astype("float64")
        return long_df

    def plot_growth_rates(self, df, xlim, ylim):
        """
        - Parameters: df (Pandas dataframe), xlim (int), ylim (int)
          - Expects the df to have a column "n" and growth rates.
          - Typically, df should be generated using the object's
            rate_comparison_df() method.
        - Returns a seaborn plot with x-axis "N" and y-axis "Runtime"
          describing the provided growth rates. Provided xlim and
          ylim are used to limit the axes.
        """
        data = self.convert_to_long(df)
        g = sns.relplot(x="n",
                        y="value",
                        data=data,
                        hue="rate",
                        kind="line")
        g.set(xlim=(0, xlim),
              ylim=(0, ylim),
              title="Growth rates",
              xlabel="N",
              ylabel="Runtime")
        return g
