# Analysis Process

## Step 1: Project Structure

```bash
# Find entry points
Find files: **/main.{ts,js,py,go}
Find files: **/app.{ts,js,py}
Find files: **/index.{ts,js}

# Find routes/controllers
Find files: **/routes/**/*.{ts,js}
Find files: **/controllers/**/*.{ts,js}
Search text: @Controller|@Get|@Post|router\.|app\.get
```

## Step 2: Data Models

```bash
# Database schemas
Find files: **/models/**/*.{ts,js,py}
Find files: **/schema*.{ts,js,py,sql}
Find files: **/migrations/**/*
Search text: @Entity|class.*Model|schema\s*=
```

## Step 3: Business Logic

```bash
# Services and logic
Find files: **/services/**/*.{ts,js}
Search text: async.*function|export.*class
```

## Step 4: Authentication & Security

```bash
# Auth patterns
Find files: **/auth/**/*
Find files: **/guards/**/*
Search text: @Guard|middleware|passport|jwt
```

## Step 5: External Integrations

```bash
# External calls
Search text: fetch\(|axios\.|HttpService|request\(
Find files: **/integrations/**/*
Find files: **/clients/**/*
```

## Step 6: Configuration

```bash
# Config files
Find files: **/*.config.{ts,js}
Find files: **/.env*
Find files: **/config/**/*
```

## Quick Reference

| Pattern | Purpose |
|---------|---------|
| `**/main.{ts,js,py}` | Entry points |
| `**/routes/**/*` | API routes |
| `**/models/**/*` | Data models |
| `@Controller\|@Get` | NestJS patterns |
| `router.\|app.get` | Express patterns |
