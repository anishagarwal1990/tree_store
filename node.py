from abc import ABCMeta, abstractmethod

class IReadDb(metaclass=ABCMeta):
    """
    Interface to time-series data
    """

    @abstractmethod
    def select_all(self, query):
        """
        Query for time-series data
        :param query: IQuery
            tskey, startTime, endTime
        :return: time-series data corresponding to s from [startTime, endTime)
        """
        raise NotImplementedError("Base class method not implemented")


    @abstractmethod
    def select_all_union(self, qset):
        """
        gets union of data from query using the given query set
        :param qset: query set
        :return: union of selectAll(q) where q in qset
        """
        raise NotImplementedError("Base class method not implemented")

    @abstractmethod
    def count(self, query):
        """
        Get the number of data points for time-series s from (startTime, endTime)
        :param query: IQuery
            tskey, startTime, endTime
        :return: unsigned long
        """
        raise NotImplementedError("Base class method not implemented")


    @abstractmethod
    def estimate_size_mb(self, query):
        """
        Estimate the size in MB of the given query
        :param query : IQuery
            tskey, starTime, endTime
        :return double  >= 0
        """
        raise NotImplementedError("Base class method not implemented")
