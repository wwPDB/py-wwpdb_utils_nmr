
// Generated from /data/git/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/BarePDBParser.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"




class  BarePDBParser : public antlr4::Parser {
public:
  enum {
    Integer = 1, Float = 2, COMMENT = 3, Hetatm_decimal = 4, Integer_concat_alt = 5, 
    Float_concat_2 = 6, Float_concat_3 = 7, Atom = 8, Hetatm = 9, Ter = 10, 
    End = 11, Simple_name = 12, Null_value = 13, SPACE = 14, ENCLOSE_COMMENT = 15, 
    SECTION_COMMENT = 16, LINE_COMMENT = 17, Any_name = 18, SPACE_CM = 19, 
    RETURN_CM = 20
  };

  enum {
    RuleBare_pdb = 0, RuleComment = 1, RuleCoordinates = 2, RuleAtom_coordinate = 3, 
    RuleAtom_num = 4, RuleAtom_name = 5, RuleXyz = 6, RuleX_yz = 7, RuleXy_z = 8, 
    RuleX_y_z = 9, RuleUndefined = 10, RuleNumber = 11, RuleTerminal = 12, 
    RuleEnd = 13
  };

  explicit BarePDBParser(antlr4::TokenStream *input);

  BarePDBParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~BarePDBParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Bare_pdbContext;
  class CommentContext;
  class CoordinatesContext;
  class Atom_coordinateContext;
  class Atom_numContext;
  class Atom_nameContext;
  class XyzContext;
  class X_yzContext;
  class Xy_zContext;
  class X_y_zContext;
  class UndefinedContext;
  class NumberContext;
  class TerminalContext;
  class EndContext; 

  class  Bare_pdbContext : public antlr4::ParserRuleContext {
  public:
    Bare_pdbContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<CoordinatesContext *> coordinates();
    CoordinatesContext* coordinates(size_t i);
    std::vector<TerminalContext *> terminal();
    TerminalContext* terminal(size_t i);
    std::vector<EndContext *> end();
    EndContext* end(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Bare_pdbContext* bare_pdb();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  CoordinatesContext : public antlr4::ParserRuleContext {
  public:
    CoordinatesContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<Atom_coordinateContext *> atom_coordinate();
    Atom_coordinateContext* atom_coordinate(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CoordinatesContext* coordinates();

  class  Atom_coordinateContext : public antlr4::ParserRuleContext {
  public:
    Atom_coordinateContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    Atom_numContext *atom_num();
    std::vector<Atom_nameContext *> atom_name();
    Atom_nameContext* atom_name(size_t i);
    XyzContext *xyz();
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer_concat_alt();
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    antlr4::tree::TerminalNode *Float_concat_2();
    std::vector<UndefinedContext *> undefined();
    UndefinedContext* undefined(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_coordinateContext* atom_coordinate();

  class  Atom_numContext : public antlr4::ParserRuleContext {
  public:
    Atom_numContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Atom();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Hetatm();
    antlr4::tree::TerminalNode *Hetatm_decimal();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_numContext* atom_num();

  class  Atom_nameContext : public antlr4::ParserRuleContext {
  public:
    Atom_nameContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer_concat_alt();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Atom_nameContext* atom_name();

  class  XyzContext : public antlr4::ParserRuleContext {
  public:
    XyzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    X_yzContext *x_yz();
    Xy_zContext *xy_z();
    X_y_zContext *x_y_z();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  XyzContext* xyz();

  class  X_yzContext : public antlr4::ParserRuleContext {
  public:
    X_yzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    NumberContext *number();
    antlr4::tree::TerminalNode *Float_concat_2();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  X_yzContext* x_yz();

  class  Xy_zContext : public antlr4::ParserRuleContext {
  public:
    Xy_zContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float_concat_2();
    NumberContext *number();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Xy_zContext* xy_z();

  class  X_y_zContext : public antlr4::ParserRuleContext {
  public:
    X_y_zContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float_concat_3();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  X_y_zContext* x_y_z();

  class  UndefinedContext : public antlr4::ParserRuleContext {
  public:
    UndefinedContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Null_value();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  UndefinedContext* undefined();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Integer();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  TerminalContext : public antlr4::ParserRuleContext {
  public:
    TerminalContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Ter();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    antlr4::tree::TerminalNode *Atom();
    antlr4::tree::TerminalNode *Hetatm();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  TerminalContext* terminal();

  class  EndContext : public antlr4::ParserRuleContext {
  public:
    EndContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *End();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  EndContext* end();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

