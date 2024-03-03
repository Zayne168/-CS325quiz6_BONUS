from abc import ABC, abstractmethod

# We can see SRP utilized through the usage of seperate classes for the User, Activity,
#ActivityMonitor, DataStorage and Display.

#We can see OCP through the ActivityMonitor. We can add more activities but changing 
#what any function does is not fully easy

#We can see LSP through ensuring that all of the activity subclasses work for 
#the functions of the activity main-class. which is not super functional right now.

#We can see ISp through seperating data collection/storage and display. A user should 
#not be able to access the functions that control data collection(so that maybe 
#they do not "hack in" and say they are doing more exercise than actual etc) but 
#should be able to see the data collected through display. 

#We can see DIP through the initialization of the ActivityMonitor. The usage of data 
#storage and display within the initialization keeps those two dependencies accessable 
#for testing while making the ActivityMonitor.

#I am low on time to finish the full implementation. Most of it is here, but I do not 
#store any of the data. If I were I would just store it in .txt or CSV files 
#and then use read/write functionality to access them. 
#I also utilize sample data in the activity subclasses instead of full information 
#that gets read in to make this code simpler
#


class User:
    def __init__(self, name):
        self.name = name

class Activity(ABC):
    @abstractmethod
    def track_activity(self):
        pass
class Walking(Activity):
    def track_activity(self):
        # Sample info in an undermade class
        return {
            'type': 'Walking',
            'steps': 2500,
            'distance': 2.0,
            'calories': 150
        }
class Running(Activity):
    def track_activity(self):
        # Sample info in an undermade class
        return {
            'type': 'Running',
            'steps': 5000,
            'distance': 5.0,
            'calories': 300
        }

class ActivityMonitor:
    def __init__(self, user, data_storage, display):
        self.user = user
        self.data_storage = data_storage
        self.display = display
    def collect_activity_data(self, activity):
        activity_data = activity.track_activity()
        self.data_storage.store_activity_data(activity_data)
        self.display.notify(activity_data)
class DataStorage:
    def store_activity_data(self, activity_data):
        print(f"Storing activity data: {activity_data}")
        #this could be implemented through with writing data to .txt files if I had time.

class Display(ABC):
    @abstractmethod
    def notify(self, activity_data):
        pass
class ConsoleDisplay(Display):
    def notify(self, activity_data):
        print(f"Displaying activity data for {activity_data['type']}: {activity_data}")
class MobileAppDisplay(Display):
    def notify(self, activity_data):
        print(f"Showing activity data on mobile app for {activity_data['type']} activity: {activity_data}")
#We could add more Display types if wanted due to the built-in ISP and SRP usage. 

def main():
  user = User("Alice")
  data_storage = DataStorage()
  console_display = ConsoleDisplay()
  activity_monitor = ActivityMonitor(user, data_storage, console_display)
    #sample data and sample usage
  walking_activity = Walking()
  running_activity = Running()
  activity_monitor.collect_activity_data(walking_activity)
  activity_monitor.collect_activity_data(running_activity)
if __name__ == "__main__":
  main()