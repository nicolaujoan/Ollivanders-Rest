# This class has two methods for extracting the occurrences of a specified product
# the first one takes all the occurrences
# the second one is for the case when in a given day we have multiple instances of a product
# the second is an overloaded method so we have installed 'multipledispatch' package to do it

from multipledispatch import dispatch


class TestAutomata:

    """
    :param -> str(fileName), str(itemName); the file name in our case will be stdout.gr
        and the item name may vary depending on the product we specify
    :return list(expectedReps) -> all occurrences of a product
    """
    @staticmethod
    @dispatch(str, str)
    def getExpectedReps(fileName, itemName):

        expectedReps = []

        try:
            file = open(fileName, "r")

        except FileNotFoundError:
            print("can't open the specified file")

        else:
            hasStarted = False
            for line in file:
                line = line.strip()
                if line == "-------- day 1 --------":
                    hasStarted = True
                if hasStarted:
                    if itemName in line:
                        expectedReps.append(line)
            file.close()

        return expectedReps

    """
    helper method to initialize the expectedReps for every instance of the same product
    @:param -> int(numInstances)
    @:return -> list(container for expectedReps, are empty sublists in a list)
    """
    @staticmethod
    def __initializeReps(numInstances):
        expectedReps = []
        for i in range(numInstances):
            expectedReps.append([])
        return expectedReps

    """
        :param -> str(fileName), str(itemName), int(instancesPerDay); 
            the file name in our case will be stdout.gr
            and the item name may vary depending on the product we specify
            the instancesPerDay will depend on the product too
        :return list(expectedReps) -> all occurrences of every instance of a product
            it will be a list of sublists
        """
    @staticmethod
    @dispatch(str, str, int)
    def getExpectedReps(fileName, itemName, instancesPerDay):

        expectedReps = TestAutomata.__initializeReps(instancesPerDay)
        index = 0

        try:
            file = open(fileName, "r")

        except FileNotFoundError:
            print("can't open the specified file")

        else:
            hasStarted = False
            for line in file:
                line = line.strip()
                if line == "-------- day 1 --------":
                    hasStarted = True
                if hasStarted:
                    if itemName in line:
                        expectedReps[index].append(line)
                        index += 1
                        if index == instancesPerDay:
                            index = 0
            file.close()

        return expectedReps
