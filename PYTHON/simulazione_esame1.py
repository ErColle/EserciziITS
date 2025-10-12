class AppointmentScheduler: 
    def __init__(self):
        self.appointments = {}  # nome corretto del dizionario
        
    def schedule_appointment(self, app_id: str, data: str):
        if app_id in self.appointments:
            return "Errore: appuntamento esiste già."
        else:
            self.appointments[app_id] = {"programmato": True, "data": data} 
            return {app_id: self.appointments[app_id]}

    def reschedule_appointment(self, app_id: str, nuova_data: str):
        if app_id not in self.appointments:
            return "Errore: appuntamento non esiste."
        else:
            self.appointments[app_id]["data"] = nuova_data
            return {app_id: self.appointments[app_id]}
        
    def cancel_appointment(self, app_id: str):
        if app_id not in self.appointments:
            return "Errore: appuntamento non esiste."
        else:
            self.appointments[app_id]["programmato"] = False
            return {app_id: self.appointments[app_id]}
        
    def remove_appointment(self, app_id: str):
        if app_id not in self.appointments:
            return "Errore: appuntamento non esiste."
        else:
            removed = {app_id: self.appointments.pop(app_id)}
            return removed
        
    def list_appointments(self):
        return self.appointments
        
    def get_appointment(self, app_id: str): 
        if app_id not in self.appointments:
            return "Errore: appuntamento non esiste."
        return {app_id: self.appointments[app_id]}


    

