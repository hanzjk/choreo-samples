import ballerina/http;

type Greeting record {
    string 'from;
    string to;
    string message;
};
configurable string name = ?;


service / on new http:Listener(8090) {
    resource function get .() returns Greeting {
        Greeting greetingMessage = {"from" : "Choreo", "to" : "hansi", "message" : "Welcome to Choreo!"};
        return greetingMessage;
    }
}
