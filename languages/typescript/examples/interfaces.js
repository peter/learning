function greet(person) {
    return "Hello " + person.firstName + " " + person.lastName;
}
console.log(greet({ firstName: 'Peter', lastName: 'Marklund' }));
