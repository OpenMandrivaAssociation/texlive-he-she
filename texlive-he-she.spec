# revision 24938
# category Package
# catalog-ctan /macros/latex/contrib/he-she
# catalog-date 2011-02-16 08:41:21 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-he-she
Version:	1.0
Release:	5
Summary:	Alternating pronouns to aid to gender-neutral writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/he-she
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements a version of semi-automatic pronoun
switching for writing gender-neutral (and possibly annoying)
prose. It has upper- and lowercase versions of switching
pronouns for all case forms, plus anaphoric versions that
reflect the current gender choice.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/he-she/he-she.sty
%doc %{_texmfdistdir}/doc/latex/he-she/README
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.pdf
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-4
+ Revision: 758889
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-3
+ Revision: 752545
- Rebuild to reduce used resources
- texlive-he-she

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718614
- texlive-he-she
- texlive-he-she
- texlive-he-she
- texlive-he-she

