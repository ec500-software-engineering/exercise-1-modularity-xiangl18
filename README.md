# exercise-1-modularity-xiangl18
## Modularity

System diagram is as followed:  
![image](https://github.com/ec500-software-engineering/exercise-1-modularity-xiangl18/blob/master/Health_Monitor_system_diagram.png)  
As we can see, there are five parts: 
1. Input Analyzer
2. Storage System
3. AI Module
4. Alert System
5. User Interface  
Input Analyzer reads data from example file, there are different data types: blood pressure, blood oxygen, pulse.  

## Quick run  
To run this program, please directly input 
```python
python main.py 
```
in your command line.  
## Pros & Cons  
### Pros:  
* we can easily achieve running and connnecting different modules, and also communicating between mudules.  
* By using threading and queue, We can also support multi threads dequeue and enqueue easily, simplify the complexity of multithread programming.
* We can support event trigger, events will be processed when they enqueue.

### Cons:  
* The space might need to be dilated when queue need more space, and a fixed queue is hard to decide its capacity.  
* Overflow might happen.
* Could consider implementing callback.
