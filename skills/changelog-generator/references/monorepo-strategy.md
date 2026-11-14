# Monorepo Changelog Strategy

## Approaches

| Strategy | When to use | Tradeoff |
|----------|-------------|----------|
| Single root changelog | Product-wide releases, small teams | Simple, but loses package-level detail |
| Per-package changelogs | Independent versioning, large teams | Clear ownership, but harder to see the full picture |
| Hybrid model | Root summary + package-specific details | Best of both, more maintenance |

## Commit scoping pattern

Use scoped conventional commits so each package can be filtered:

```
feat(payments): add Stripe webhook handler
fix(auth): handle expired refresh tokens
chore(infra): bump base Docker image
```

**Rules:**
- The scope must match a package or directory name exactly.
- Unscoped commits go only to the root changelog.
- Changes that span several packages get separate scoped commits (not one large commit).

## Filtering for package releases

```bash
# Generate changelog for 'payments' package only
git log v1.3.0..HEAD --pretty=format:'%s' | grep '^[a-z]*\(payments\)' | \
  python3 scripts/generate_changelog.py --next-version v1.4.0 --format markdown
```

## Ownership model

- Package maintainers own their scoped changelog.
- The platform/infra team owns the root changelog.
- CI enforces the scope on every commit that touches package directories.
- The root changelog aggregates breaking changes from all packages, for visibility.
