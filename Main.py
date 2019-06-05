from EducationSystem import EducationSystem

if __name__ == "__main__":
    # @TODO: Make all the fields private(i.e. Use __ before each field name)
    educationSystem = EducationSystem.getInstance()
    educationSystem.initializeSystem()
    educationSystem.printDatabase()