from abc import ABCMeta, abstractmethod

class INode(metaclass=ABCMeta):
    """
    Interface to node class. Sub-classes have functionality to take vectors and
    bucket them according to a hash method
    """

    @abstractmethod
    def generate_hash(self, vector):
        """
        returns the hash of a vector
        :param vector: numpy array
        :return: hash_signature of vector
        """
        raise NotImplementedError("Base class method not implemented")

    @abstractmethod
    def is_leaf_node(self):
        """
        gets union of data from query using the given query set
        :param qset: query set
        :return: boolean indicating whether instance is a leaf node
        """
        raise NotImplementedError("Base class method not implemented")

    @abstractmethod
    def get_child_node(self, child_hash):
        """
        gets child_node object based on hash of child
        :param qset: child_hash
        :return: child node object
        """
        raise NotImplementedError("Base class method not implemented")

    @abstractmethod
    def get_parent_node(self, parent_hash):
        """
        get parent_node based on hash of parent
        :param qset: parent_hash
        :return: parent node object
        """
        raise NotImplementedError("Base class method not implemented")

