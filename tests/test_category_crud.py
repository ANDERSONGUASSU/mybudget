"""
    Testes para o CRUD de categorias
"""

import sys
import os
from controllers.category_controllers import (
    create_category,
    get_categories,
    get_category,
    get_categories_for_type,
    update_category,
    delete_category
)

# Adicionando o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def test_create_category():
    """
    Testa a criação de categorias
    """
    # Criar uma categoria de receita
    income_cat = create_category("Teste Receita", "income", "#00FF00")
    assert income_cat is not None
    assert income_cat['name'] == "Teste Receita"
    assert income_cat['type'] == "income"

    # Criar uma categoria de despesa
    expense_cat = create_category("Teste Despesa", "expense", "#FF0000")
    assert expense_cat is not None
    assert expense_cat['name'] == "Teste Despesa"
    assert expense_cat['type'] == "expense"

    print("✅ Teste de criação de categorias concluído com sucesso!")
    return income_cat, expense_cat


def test_get_categories(income_cat_id, expense_cat_id):
    """
    Testa a obtenção de categorias
    """
    # Obter todas as categorias
    all_cats = get_categories()
    assert isinstance(all_cats, list)
    assert len(all_cats) > 0

    # Obter categoria específica
    income_cat = get_category(income_cat_id)
    assert income_cat is not None
    assert income_cat['id'] == income_cat_id

    # Obter categorias por tipo
    income_cats = get_categories_for_type('income')
    assert isinstance(income_cats, list)
    assert any(cat['id'] == income_cat_id for cat in income_cats)

    expense_cats = get_categories_for_type('expense')
    assert isinstance(expense_cats, list)
    assert any(cat['id'] == expense_cat_id for cat in expense_cats)

    print("✅ Teste de obtenção de categorias concluído com sucesso!")


def test_update_category(category_id):
    """
    Testa a atualização de uma categoria
    """
    # Obter categoria original
    original_cat = get_category(category_id)
    assert original_cat is not None

    # Atualizar nome e cor
    updated_cat = update_category(category_id, name="Categoria Atualizada", color="#0000FF")
    assert updated_cat is not None
    assert updated_cat['id'] == category_id
    assert updated_cat['name'] == "Categoria Atualizada"
    assert updated_cat['color'] == "#0000FF"

    # Verificar se a atualização persistiu
    verified_cat = get_category(category_id)
    assert verified_cat['name'] == "Categoria Atualizada"

    print("✅ Teste de atualização de categoria concluído com sucesso!")
    return updated_cat


def test_delete_category(category_id):
    """
    Testa a exclusão de uma categoria
    """
    # Verificar se a categoria existe
    cat = get_category(category_id)
    assert cat is not None

    # Excluir a categoria
    result = delete_category(category_id)
    assert result is True

    # Verificar se a categoria foi excluída
    deleted_cat = get_category(category_id)
    assert deleted_cat is None

    print("✅ Teste de exclusão de categoria concluído com sucesso!")


def run_tests():
    """
    Executa todos os testes
    """
    print("🧪 Iniciando testes de CRUD de categorias...")

    # Teste de criação
    income_cat, expense_cat = test_create_category()

    # Teste de obtenção
    test_get_categories(income_cat['id'], expense_cat['id'])

    # Teste de atualização
    updated_cat = test_update_category(income_cat['id'])

    # Teste de exclusão
    test_delete_category(expense_cat['id'])

    # Excluir a categoria atualizada
    test_delete_category(updated_cat['id'])

    print("🎉 Todos os testes de CRUD de categorias concluídos com sucesso!")


if __name__ == "__main__":
    run_tests()
