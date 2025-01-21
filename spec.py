class Param:
    def __init__(self,name: str,tp: str,required: bool,desc: str):
        self.name=name
        self.tp=tp
        self.required=required
        self.desc=desc

class Struct:
    def __init__(self,name: str,params: 'list[Param]'):
        self.name=name
        self.params=params

    def addParam(self,param):
        self.params.append(param)

class Interface:
    def __init__(self,name: str,tp: bool,desc: str,params: 'list[Param]'):
        self.name=name
        self.tp=tp
        self.desc=desc
        self.params=params
