from django.db import models

# Create your models here.

class Property_details(models.Model):
    id,name,addr,state_name,state_id,city = 0,'','','',0,''
    
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=255)
    p_addr = models.CharField(max_length=255)
    p_state_name = models.CharField(max_length=255)
    p_city = models.CharField(max_length=255)
    
    def clean(self):
        self.p_state_name = self.p_state_name.casefold()
        self.p_addr = self.p_addr.casefold()
        self.p_name = self.p_name.casefold()
        self.p_city = self.p_city.casefold()
        
    
    def  __str__(self):
        return "p_id :"+str(self.p_id)+", p_name :"+self.p_name+", p_address "+self.p_addr+", p_state_name "+self.p_state_name+", p_city "+self.p_city

class State_details(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=255)
    
