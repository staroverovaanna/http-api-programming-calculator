# http-api-programming-calculator

To run flask app: 
`flask run`

To calculate your expression: 

`curl 127.0.0.1:5000/calculate --header 'Content-Type: application/json' -X POST --data '{"expression": "-2 * (3 + 4) - 5 / 2"}'`

Returns: 
- `{"response":"The answer is -8.0"}`
- `{"error":"Message: Division by zero: 2.0 / 0.0, status 400 Bad request"}`

Enter your expression here


<img width="405" alt="Снимок экрана 2024-11-07 в 19 05 50" src="https://github.com/user-attachments/assets/724a5f48-1109-47fc-9e9e-ca57ae5a3a1e">

Get results


<img width="409" alt="Снимок экрана 2024-11-07 в 19 06 06" src="https://github.com/user-attachments/assets/83ea7602-be2b-4d8a-be13-415c366dd36e">
