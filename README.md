# Vacinação

## Rotas

- POST

  Responsável pela inserção de dados no banco de dados.

  **Corpo da requisição**

  ```json
  {
    "cpf": "01234567891",
    "name": "Chrystian",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
  }
  ```

  A requisição deve conter obrigatóriamente os campos _cpf_, _name_, _vaccine_name_ e _health_unit_name_ e devem ser todas _string_, caso contrário retornará o _status code 400 (BAD REQUEST)_. O campo _cpf_ deve conter 11 caracteres, caso contrário também retornará _status code 400 (BAD REQUEST)_.

  O campo _cpf_ deve ser unico, retornando _status code 409 (CONFLICT)_ caso o cpf já exista no banco de dados. Qualquer outro tipo de campo passado irá ser ignorado.

  **Resposta**

  **_Status: 201 CREATED_**

  ```json
  {
    "cpf": "01234567891",
    "name": "Chrystian",
    "first_shot_date": "Fri, 29 Oct 2021 16:36:13 GMT",
    "second_shot_date": "Thu, 27 Jan 2022 16:36:13 GMT",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
  }
  ```

  O campo _first_shot_date_ registra automaticamente a data atual da requisição, e o campo _second_shot_date_ calcula automaticamente a data 90 dias após a data do _first_shot_date_.

* GET

  Obtem todos os dados do banco de dados.

  ```json
  [
    {
      "cpf": "01234567891",
      "name": "Chrystian",
      "first_shot_date": "Fri, 29 Oct 2021 16:30:31 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:30:31 GMT",
      "vaccine_name": "Pfizer",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "19876543210",
      "name": "Cauan",
      "first_shot_date": "Fri, 29 Oct 2021 16:31:30 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:31:30 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "54221194161",
      "name": "Eduardo",
      "first_shot_date": "Fri, 29 Oct 2021 16:35:24 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:35:24 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    }
  ]
  ```
