# EARS Format

## EARS syntax

EARS (Easy Approach to Requirements Syntax) is a set of fixed sentence patterns that keeps requirements clear and unambiguous.

### Basic patterns

**Ubiquitous (always true)**
```
The system shall [action].
```

**Event-driven**
```
When [trigger], the system shall [action].
```

**State-driven**
```
While [state], the system shall [action].
```

**Conditional**
```
While [state], when [trigger], the system shall [action].
```

**Optional**
```
Where [feature enabled], the system shall [action].
```

## Example observations

### Authentication

**OBS-AUTH-001: Login flow**
```
While credentials are valid, when POST /auth/login is called,
the system shall return JWT access token (15m) and refresh token (7d).
```

**OBS-AUTH-002: Token refresh**
```
While refresh token is valid, when POST /auth/refresh is called,
the system shall issue new access token.
```

**OBS-AUTH-003: Invalid token**
```
When expired or invalid token is provided,
the system shall return 401 Unauthorized.
```

### User management

**OBS-USER-001: User creation**
```
While email is unique, when POST /users is called with valid data,
the system shall create user with bcrypt-hashed password (rounds=12).
```

**OBS-USER-002: Email validation**
```
When email format is invalid,
the system shall return 400 with error message "Invalid email format".
```

### Input validation

**OBS-INPUT-001: Required fields**
```
When required fields are missing,
the system shall return 400 with field-specific error messages.
```

## Quick reference

| Type | Pattern | Example trigger |
|------|---------|-----------------|
| Ubiquitous | shall [action] | Always true |
| Event | When [X], shall | On button click |
| State | While [X], shall | While logged in |
| Conditional | While [X], when [Y], shall | While admin, when delete |
| Optional | Where [X], shall | If feature enabled |
