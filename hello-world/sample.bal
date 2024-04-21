import ballerina/http;
import ballerina/os;
import ballerina/os;

service /hello on new http:Listener(8090) {
    resource function get greeting() returns json|error {
        string serviceURL = os:getEnv("SVC_URL");
        string tokenURL = os:getEnv("TOKEN_URL");
        string consumerKey = os:getEnv("CONSUMER_KEY");
        string consumerSecret = os:getEnv("CONSUMER_SECRET");
        io:println("url:"+serviceURL);
        http:Client httpClient = check new http:Client(serviceURL, {
            auth: {
                tokenUrl: tokenURL,
                clientId: consumerKey,
                clientSecret: consumerSecret
            }
        });
    

        json payload = check httpClient->get("/");

        
            return payload;
    }
    
}
