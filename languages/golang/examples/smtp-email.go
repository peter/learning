package main

import (
	"fmt"
	"net/smtp"
	"os"
	"strings"
)

func EnvWithDefault(env string, defaultValue string) string {
	value := os.Getenv(env)
	if value == "" {
		return defaultValue
	}
	return strings.TrimSpace(value)
}

func sendEmail(to []string, subject, body string) error {
	from := "peter.marklund@seenthis.se"
	message := []byte(strings.Join([]string{
		fmt.Sprintf("From: %s", from),
		fmt.Sprintf("To: %s", strings.Join(to, ",")),
		fmt.Sprintf("Subject: %s", subject),
		"",
		body,
	}, "\r\n"))

	// Authentication
	smtpHost := EnvWithDefault("SMTP_HOST", "smtp.gmail.com")
	smtpPort := "587"
	smtpUsername := os.Getenv("SMTP_USERNAME")
	smtpPassword := os.Getenv("SMTP_PASSWORD")
	auth := smtp.PlainAuth("", smtpUsername, smtpPassword, smtpHost)

	// Send email
	err := smtp.SendMail(
		smtpHost+":"+smtpPort,
		auth,
		from,
		to,
		message,
	)

	return err
}

func main() {
	// Example usage
	to := []string{"peter@marklunds.com"}
	subject := "Test SMTP Email"
	body := "This is a test email sent from Go using SMTP."

	err := sendEmail(to, subject, body)
	if err != nil {
		fmt.Printf("Failed to send email: %v\n", err)
		return
	}
	fmt.Println("Email sent successfully!")
}
