import microsoft.aspnet.signalr.client.Logger;
import microsoft.aspnet.signalr.client.LogLevel;

public class PrintLogger implements Logger {
	@Override
	public void log(String message, LogLevel level) {
		System.out.println(message);
	}
}
