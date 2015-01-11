import microsoft.aspnet.signalr.client.*;
import microsoft.aspnet.signalr.client.hubs.*;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import org.zeromq.ZMQ;

public class MojioObserver //extends ConfigRepository<VHostItem>
{
	private static final ZMQ.Context context = ZMQ.context(1);

	public static void main(String [] args)
	{
		final ZMQ.Socket sock = context.socket(ZMQ.PUSH);
		sock.bind("ipc:///tmp/mojio-observer");

		Logger logger = new NullLogger();
		//Logger logger = new PrintLogger();

		HubConnection conn = new HubConnection("http://data.api.hackthedrive.com/v1", null, true, logger);
		HubProxy proxy = conn.createHubProxy("ObserverHub");

		System.out.println("connecting");
		try {
			conn.start().get();
		} catch (Exception e) {
			e.printStackTrace();
		}

		System.out.println("connected");

		System.out.println("subscribing");
		proxy.invoke("Subscribe", "a53f8e61-4eec-42df-962c-42e2c404726b");

		System.out.println("subscribed");

		proxy.on("UpdateEntity", new SubscriptionHandler1<JsonElement>() {
			@Override
			public void run(JsonElement msg) {
				Gson gson = new Gson();
				String str = gson.toJson(msg);
				System.out.println("IN: " + str);
				try {
					byte[] buf = str.getBytes("utf-8");
					sock.send(buf, 0);
				} catch (Exception e) {
					System.out.println("failed to send");
				}
			}
		}, JsonElement.class);

		System.out.println("waiting for events");
	}
}
