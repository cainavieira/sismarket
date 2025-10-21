# Guia de Contribuição – sismarket

Obrigado por considerar contribuir com este projeto!  
Antes de enviar mudanças, siga estas orientações para mantermos um repositório limpo e organizado.

---

## 📌 Commits

Este projeto usa o padrão **Conventional Commits**.  
Formato:

```
<tipo>(<escopo opcional>): <descrição curta no imperativo>
```

### Tipos aceitos
- feat: nova funcionalidade
- fix: correção de bug
- docs: mudanças na documentação (README, CHANGELOG, CONTRIBUTING etc.)
- style: formatação sem alterar comportamento
- refactor: alteração interna sem mudança de comportamento externo
- perf: otimização de desempenho
- test: adição ou ajuste de testes
- build: mudanças em build/dependências
- ci: mudanças em integração contínua (GitHub Actions, etc.)
- chore: manutenção e tarefas auxiliares
- revert: reverte commit anterior

### Exemplos
```
feat(auth): adiciona login por token JWT
fix(api): corrige erro 500 no cadastro de usuário
docs(readme): adiciona seção de Roadmap
chore: adiciona .gitignore (template Python)
test: cria teste de sanidade em tests/test_sisrel_basico.py
```

---

## 📂 Estrutura recomendada de pastas
- `src/` → código principal
- `tests/` → testes automatizados
- `docs/` → documentação
- `.github/` → templates e metadados do GitHub

---



## 🗺️ Roadmap
Confira o ROADMAP antes de propor mudanças para alinhar com o que está planejado.

---

## 🤝 Como contribuir
- Faça um fork
- Crie uma branch (git checkout -b ou git switch -c feature/nova-feature)
- Commit suas mudanças (git commit -m 'Adiciona nova feature')
- Faça push (git push origin feature/nova-feature)
- Abra um Pull Request

Obrigado por ajudar a melhorar o **sismarket** 🚀
