import sys

class customexception(Exception):

    def __init_(self,error_message,erro_details:sys):
        self.error_message
        _,_,exec_tab = erro_details.exec_info()

        self.lineno = exec_tab.tb_lineno
        self.file_name= exec_tab.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number  [{1}] errormessage [{2}]".format(self.file_name,self.lineno,str(self.error_message)) 
    

if __name__ == "__main__" :
    try:
        pass
    except Exception as e:
        #print(e)
        raise customexception(e,sys)
 