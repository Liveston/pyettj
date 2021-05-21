import pytest
import sys

path = "../pyettj/"
sys.path.append(path)

import ettj
data = "2021/05/18"

class TestClass():

    def test_ettj(self):
        self.ettj_dataframe = ettj.get_ettj(data)
        self.curvas = self.ettj_dataframe.columns.tolist()[1:]
        self.curva = self.curvas[-2] #libor
        return self.ettj_dataframe, self.curva

    def test_plot_ettj(self):
        self.ettj_dataframe, self.curva = self.test_ettj()
        ettj.plot_ettj(self.ettj_dataframe.drop(self.ettj_dataframe.columns[0],axis=1), self.curva, data)

    def test_raises(self):
        with pytest.raises(Exception) as error1:
            ettj.get_ettj(18)
        assert str(error1.value) == "O parametro data deve ser em formato string, exemplo: '18/05/2021'"
        with pytest.raises(Exception) as error2:
            ettj.get_ettj("teste")
        assert str(error2.value) == "O parametro data deve ser em formato string, exemplo: '18/05/2021'"  

TestClass()