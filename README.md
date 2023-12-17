# http-api-programming-calculator

To run flask app: 
`flask run`

To calculate your expression: 

`curl 127.0.0.1:5000/calculate --header 'Content-Type: application/json' -X POST --data '{"expression": "-2 * (3 + 4) - 5 / 2"}'`

Returns: 
- `{"response":"The answer is -8.0"}`
- `{"error":"Message: Division by zero: 2.0 / 0.0, status 400 Bad request"}`