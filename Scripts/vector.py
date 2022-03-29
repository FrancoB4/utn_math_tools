from typing import Union
import numpy as np


class Vector:

    def __init__(self, values: Union[list, tuple, iter]) -> None:
        self.values = tuple(values)
        self.n_dim = len(self.values)
        self.module = sum([x ** 2 for x in self.values])**(1/2)

    def pp(self, other_vector: 'Vector') -> int:
        """_summary_

        Args:
            other_vector (Vector): other vector.
        """
        try:
            if other_vector.n_dim == self.n_dim:
                return sum([i * k for i, k in zip(other_vector.values, self.values)])
                # for i, k in zip(other_vector.values, self.values):
                #     aux.append(i * k)
                # return sum(aux)
            else:
                raise ValueError(f"El vector ingresado es de dimensión "
                                 f"[{other_vector.n_dim}], se esperaba [{self.n_dim}]")
        except ValueError as ve:
            print(ve)
            return 0

    def pe(self, a: int) -> object:
        """_summary_

        Args:
            a (int):
        """
        return Vector([i * a for i in self.values])

    def angle(self, other_vector: 'Vector') -> float:
        """_summary_

        Args:
            other_vector (Vector): other vector.
        """
        return np.cos(self.pp(other_vector) / (self.module * other_vector.module))


