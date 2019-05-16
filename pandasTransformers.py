from sklearn.base import BaseEstimator, TransformerMixin


# Selects numerical or categorical columns in Pandas DataFrame
class CategorySelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        print("on self")
        print(self)
        return self

    def transform(self, X):
        print("on transform")
        return X[self.attribute_names].values

#Drops specified columns in Pandas DataFrame
class CategoryDeletor(BaseEstimator, TransformerMixin):
    def __init__(self, deleted_attributes):
        self.deleted_attributes = deleted_attributes

    def fit(self, X, y=None):
        print(self)
        return self

    def transform(self, X):
        attributes = list(X.columns)
        print(attributes)
        for i in self.deleted_attributes:
            if i in attributes:
                attributes.remove(i)
                print(attributes)
        return X[attributes].values
