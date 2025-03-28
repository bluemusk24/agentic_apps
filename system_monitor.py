import psutil
import time

# Define the System Monitoring Agent class
class SystemMonitoringAgent:
    def __init__(self, cpu_threshold=5, check_interval=10):
        """
        An agent that will monitor Systems using the CPU threshold and intervals.
        Args:
            self: initialize the System Monitoring agent.
            cpu_threshold: CPU usage percentage to trigger an alert.
            check_interval: Time interval (in seconds) between checks.
        """
        self.cpu_threshold = cpu_threshold
        self.check_interval = check_interval
    
    def monitor_cpu(self, iterations=5):
        """
        Monitoring of CPU usage and alert if the threshold is exceeded
        Args:
            iterations: Number of monitoring cycles to perform before stopping
        """
        count = 0
        # Loop for specified number of iterations
        while count < iterations:
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Display memory usage with each CPU check
            self.monitor_memory()

            # if CPU usage exceeds threshold, trigger an alert high CPU.
            if cpu_usage > self.cpu_threshold:
                self.alert_high_cpu(cpu_usage)
            else:
                print(f"CPU usage is normal: {cpu_usage}%")
                
            count += 1
            if count < iterations:  # Don't sleep after the final iteration
                time.sleep(self.check_interval)   # wait for interval before next check
        
        print(f"Monitoring complete after {iterations} checks.")

    def alert_high_cpu(self, cpu_usage):
        """
        Handle high CPU usage alerts
        Args:
            cpu_usage: The current CPU usage percentage.
        """
        print(f"ALERT: High CPU usage detected {cpu_usage}%")    # display an alert message

    def monitor_memory(self):
        """
        Monitor memory usage and display the percentage used.
        """
        memory = psutil.virtual_memory()    # memory usage info
        print(f"Memory Usage: {memory.percent}%")


def main():
    # create an instance of the SystemMonitoringAgent with CPU threshold and interval.
    agent = SystemMonitoringAgent(cpu_threshold=5, check_interval=10)
    agent.monitor_cpu(iterations=5)  # Stop after 5 iterations

if __name__ == "__main__":
    main()