# SQLC, Go-Migrate, pgx Example

## Developer Setup

Depends on having Postgres installed and running (i.e. with Homebrew, Postgres.app, or Docker).

```sh
# Install dependencies
go get .

# Create Postgres database
createdb -U postgres sqlc-crud

# Run
go run main.go

# Inspect Postgres data with psql
psql -U postgres sqlc-crud

# Create schema with psql
psql -U postgres -d sqlc-crud -a -f schema.sql 
```

## Installing SQLC

```sh
go install github.com/sqlc-dev/sqlc/cmd/sqlc@latest
# Make sure you have ~/go/bin in your PATH:
export PATH=$PATH:~/go/bin
```

## Configuring SQLC

Create/edit the `sqlc.yaml`, `schema.sql`, and `query.sql` files

## Generating SQLC Go Code

```sh
sqlc generate
```

## Resources

* [SQLC Homepage](https://sqlc.dev/)
* [SQLC - Getting Started with Postgres](https://docs.sqlc.dev/en/stable/tutorials/getting-started-postgresql.html)
* [golang-migrate](https://github.com/golang-migrate/migrate)
* [SQLC, Go-Migrate, pgx tutorial](https://medium.com/gravel-engineering/using-sqlc-for-orm-alternative-in-golang-ft-go-migrate-pgx-b9e35ec623b2)
