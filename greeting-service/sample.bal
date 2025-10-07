import ballerina/http;
import import ballerinax/trigger.github;

type Greeting record {
    string 'from;
    string to;
    string message;
};

configurable github:ListenerConfig config = ?; 


service / on new http:Listener(8090) {
    resource function get .(string name) returns Greeting {
        Greeting greetingMessage = {"from" : "Choreo", "to" : name, "message" : "Welcome to Choreo!"};
        return greetingMessage;
    }
}
