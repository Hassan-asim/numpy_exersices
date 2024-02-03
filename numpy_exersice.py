import numpy as np

class NumPyExercises:
    def create_even_array(self):
        """
        Task 1: Create an array of all even integers from 30 to 70.
        """
        even_array = np.arange(30, 72, 2)
        return even_array

    def generate_random_numbers(self):
        """
        Task 2: Generate an array of 15 random numbers from a standard normal distribution.
        """
        random_numbers = np.random.randn(15)
        return random_numbers

    def compute_cross_product(self, matrix1, matrix2):
        """
        Task 3: Compute the cross-product of two matrices in NumPy.
        """
        cross_product = np.cross(matrix1, matrix2)
        return cross_product

    def compute_determinant(self, matrix):
        """
        Task 4: Compute the determinant of a given matrix using NumPy.
        """
        determinant = np.linalg.det(matrix)
        return determinant

    def create_random_3d_array(self):
        """
        Task 5: Create a 3x3x3 array with random values using NumPy.
        """
        random_3d_array = np.random.random((3, 3, 3))
        return random_3d_array

    def create_random_5x5_array(self):
        """
        Task 6: Create a 5x5 array with random values and find the minimum and maximum values using NumPy.
        """
        random_5x5_array = np.random.random((5, 5))
        min_value = np.min(random_5x5_array)
        max_value = np.max(random_5x5_array)
        return random_5x5_array, min_value, max_value

    def compute_statistics_along_second_axis(self, array):
        """
        Task 7: Compute the mean, standard deviation, and variance of a given array along the second axis in NumPy.
        """
        mean = np.mean(array, axis=1)
        std_deviation = np.std(array, axis=1)
        variance = np.var(array, axis=1)
        return mean, std_deviation, variance

    def run_numpy_exercises(self):
        """
        Runner method to execute NumPy exercises.
        """
        # Task 1
        task1_result = self.create_even_array()
        print("Task 1: Array of even integers from 30 to 70\n", task1_result, "\n")

        # Task 2
        task2_result = self.generate_random_numbers()
        print("Task 2: Array of 15 random numbers from a standard normal distribution\n", task2_result, "\n")

        # Task 3
        matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
        matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
        task3_result = self.compute_cross_product(matrix1, matrix2)
        print("Task 3: Cross-product of two matrices\nmatrix 1 :\n",matrix1,"\nmatrix 2 :\n",matrix2,"\ncross-product :\n", task3_result, "\n")

        # Task 4
        matrix4 = np.array([[1, 2], [3, 4]])
        task4_result = self.compute_determinant(matrix4)
        print("Task 4: Determinant of the matrix \n",matrix4,"\ndeterminent :", task4_result, "\n")

        # Task 5
        task5_result = self.create_random_3d_array()
        print("Task 5: 3x3x3 array with random values\n", task5_result, "\n")

        # Task 6
        random_5x5_array, min_value, max_value = self.create_random_5x5_array()
        print("Task 6: 5x5 array with random values\n", random_5x5_array)
        print("Minimum value:", min_value)
        print("Maximum value:", max_value, "\n")

        # Task 7
        array7 = np.random.random((4, 3, 5))
        task7_result = self.compute_statistics_along_second_axis(array7)
        print("\nTask 7: Mean, standard deviation, and variance along the second axis")
        print("Random Array:")
        print(array7)
        print("\nMean along the second axis:")
        print(task7_result[0])
        print("\nStandard Deviation along the second axis:")
        print(task7_result[1])
        print("\nVariance along the second axis:")
        print(task7_result[2])

if __name__ == "__main__":
    numpy_exercises = NumPyExercises()
    numpy_exercises.run_numpy_exercises()
